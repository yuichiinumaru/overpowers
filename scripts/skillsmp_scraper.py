import argparse
import json
import time
import sys
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def download_skill_file(github_url, dest_dir):
    """Tenta baixar o arquivo SKILL.md do GitHub."""
    if not github_url or "github.com" not in github_url:
        return False
    
    skill_name = github_url.split("/")[-1]
    final_path = os.path.join("skills", skill_name, "SKILL.md")
    if os.path.exists(final_path):
        return final_path

    raw_url = github_url.replace("github.com", "raw.githubusercontent.com").replace("/tree/", "/")
    if not raw_url.endswith("/"):
        raw_url += "/"
    raw_url += "SKILL.md"
    
    try:
        response = requests.get(raw_url, timeout=10)
        if response.status_code == 200:
            file_path = os.path.join(dest_dir, f"{skill_name}_SKILL.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            return file_path
    except Exception:
        pass
    return False

def extract_github_links(driver, skills_subset):
    extract_script = r"""
    const callback = arguments[arguments.length - 1];
    const skills = arguments[0];

    async function process() {
        const results = [];
        for (const skill of skills) {
            try {
                const resp = await fetch(skill.url);
                const html = await resp.text();
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const githubLink = Array.from(doc.querySelectorAll('a'))
                    .map(a => a.href)
                    .find(href => href.includes('github.com') && href.includes('/tree/'));
                results.push({
                    title: skill.title,
                    url: skill.url,
                    github_link: githubLink || "Not found"
                });
                await new Promise(r => setTimeout(r, 50));
            } catch (e) {
                results.push({ title: skill.title, url: skill.url, error: e.message });
            }
        }
        return results;
    }
    process().then(res => callback(res));
    """
    driver.set_script_timeout(600)
    return driver.execute_async_script(extract_script, skills_subset)

def get_skills_from_url(driver, start_url, limit, download, seen_urls):
    driver.get(start_url)
    time.sleep(5)
    
    all_cards = []
    max_extract = limit

    while len(all_cards) < max_extract:
        print(f"Extraindo cards de {driver.current_url}... (encontrados nesta URL: {len(all_cards)})", flush=True)
        cards = driver.execute_script(r"""
            return Array.from(document.querySelectorAll('a'))
                .filter(a => a.href.includes('/skills/'))
                .map(a => ({ title: a.innerText.split('\n')[0], url: a.href }))
        """)

        found_new_on_page = False
        for c in cards:
            if c['url'] not in seen_urls:
                all_cards.append(c)
                seen_urls.add(c['url'])
                found_new_on_page = True
                if len(all_cards) >= max_extract:
                    break

        if len(all_cards) >= max_extract:
            break

        clicked = driver.execute_script("""
            const btns = Array.from(document.querySelectorAll('button'));
            const nextBtn = btns.find(b => b.innerText === '→');
            if (nextBtn) {
                nextBtn.click();
                return true;
            }
            return false;
        """)
        if not clicked:
            print("Fim das páginas ou botão '→' não encontrado.", flush=True)
            break
        time.sleep(3)

    print(f"Total de {len(all_cards)} cards novos encontrados nesta URL. Extraindo links do GitHub...", flush=True)

    chunk_size = 50
    all_results = []
    for i in range(0, len(all_cards), chunk_size):
        chunk = all_cards[i:i + chunk_size]
        print(f"Processando chunk {i//chunk_size + 1} ({len(chunk)} skills)...", flush=True)
        results = extract_github_links(driver, chunk)
        all_results.extend(results)
    
    if download and all_results:
        dest_dir = "downloaded_skills"
        os.makedirs(dest_dir, exist_ok=True)
        print(f"Baixando arquivos SKILL.md para {dest_dir}...", flush=True)
        for skill in all_results:
            github_link = skill.get("github_link")
            if github_link and github_link != "Not found":
                path = download_skill_file(github_link, dest_dir)
                if path:
                    skill["local_path"] = path
                    if "skills/" in path:
                        pass
                    else:
                        print(f"  [OK] {skill['title']}", flush=True)
                else:
                    print(f"  [Falha] {skill['title']}", flush=True)
            else:
                print(f"  [Sem GitHub] {skill['title']}", flush=True)
                
    return all_results

def main():
    parser = argparse.ArgumentParser(description="Scraper para skillsmp.com")
    parser.add_argument("--keyword", type=str, help="Palavra-chave para busca")
    parser.add_argument("--urls", type=str, nargs='+', help="Lista de URLs para iniciar o scraping")
    parser.add_argument("--limit", type=int, default=10, help="Limite de skills por URL ou total")
    parser.add_argument("--all", action="store_true", help="Baixar todas as skills (limitada a 1000)")
    parser.add_argument("--download", action="store_true", help="Tentar baixar os arquivos SKILL.md")
    
    args = parser.parse_args()

    target_urls = []
    if args.urls:
        target_urls = args.urls
    elif args.keyword:
        target_urls = [f"https://skillsmp.com/?q={args.keyword}"]
    elif args.all:
        target_urls = ["https://skillsmp.com/"]
        args.limit = 1000
    else:
        print("Erro: Use --keyword, --urls ou --all.")
        sys.exit(1)
        
    driver = setup_driver()
    seen_urls = set()
    
    # Load existing to avoid re-scraping the same things in one session
    tracking_file = 'scripts/skills_found.json'
    old_data = []
    if os.path.exists(tracking_file):
        with open(tracking_file, 'r', encoding='utf-8') as f:
            old_data = json.load(f)
            for item in old_data:
                seen_urls.add(item['url'])

    all_new_results = []
    for url in target_urls:
        print(f"\nIniciando scraping da URL: {url}", flush=True)
        results = get_skills_from_url(driver, url, args.limit, args.download, seen_urls)
        all_new_results.extend(results)

    driver.quit()

    # Merge and save
    merged = {item['url']: item for item in old_data}
    for item in all_new_results:
        merged[item['url']] = item

    with open(tracking_file, 'w', encoding='utf-8') as f:
        json.dump(list(merged.values()), f, indent=4, ensure_ascii=False)

    print(f"\nFinalizado! {len(all_new_results)} novas skills processadas. Total em tracking: {len(merged)}", flush=True)

if __name__ == "__main__":
    main()
