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
    
    # Converte URL de tree para raw
    # Ex: https://github.com/user/repo/tree/main/path/to/skill
    # Para: https://raw.githubusercontent.com/user/repo/main/path/to/skill/SKILL.md
    raw_url = github_url.replace("github.com", "raw.githubusercontent.com").replace("/tree/", "/")
    if not raw_url.endswith("/"):
        raw_url += "/"
    raw_url += "SKILL.md"
    
    try:
        response = requests.get(raw_url, timeout=10)
        if response.status_code == 200:
            skill_name = github_url.split("/")[-1]
            file_path = os.path.join(dest_dir, f"{skill_name}_SKILL.md")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(response.text)
            return file_path
    except Exception:
        pass
    return False

def get_skills(keyword=None, limit=10, all_mode=False, download=False):
    driver = setup_driver()
    base_url = "https://skillsmp.com/"
    
    if all_mode:
        print("\n!!! AVISO !!!")
        print("a só tu vai baixar coisa pa caralho hein parceiro tem certeza?? ahahahahaha")
        print("Iniciando modo --all com timeout de segurança.\n")
        url = base_url
        max_extract = 50 # Limite para o modo --all
    else:
        url = f"{base_url}?q={keyword}" if keyword else base_url
        max_extract = limit

    print(f"Acessando: {url}")
    driver.get(url)
    time.sleep(5)
    
    extract_script = """
    const callback = arguments[arguments.length - 1];
    async function extract(limit) {
        const cards = Array.from(document.querySelectorAll('a')).filter(a => a.href.includes('/skills/'));
        const results = [];
        for (let i = 0; i < Math.min(cards.length, limit); i++) {
            const card = cards[i];
            const url = card.href;
            const text = card.innerText;
            try {
                const resp = await fetch(url);
                const html = await resp.text();
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const githubLink = Array.from(doc.querySelectorAll('a'))
                    .map(a => a.href)
                    .find(href => href.includes('github.com') && href.includes('/tree/'));
                results.push({
                    title: text.split('\\n')[0],
                    url: url,
                    github_link: githubLink || "Not found"
                });
            } catch (e) {
                results.push({ title: text.split('\\n')[0], url: url, error: e.message });
            }
        }
        return results;
    }
    extract(arguments[0]).then(res => callback(res));
    """
    
    print(f"Extraindo até {max_extract} skills...")
    driver.set_script_timeout(60)
    skills_data = driver.execute_async_script(extract_script, max_extract)
    driver.quit()
    
    if download and skills_data:
        dest_dir = "downloaded_skills"
        os.makedirs(dest_dir, exist_ok=True)
        print(f"Baixando arquivos SKILL.md para {dest_dir}...")
        for skill in skills_data:
            path = download_skill_file(skill.get("github_link"), dest_dir)
            if path:
                skill["local_path"] = path
                print(f"  [OK] {skill['title']}")
            else:
                print(f"  [Falha] {skill['title']}")
                
    return skills_data

def main():
    parser = argparse.ArgumentParser(description="Scraper para skillsmp.com")
    parser.add_argument("--keyword", type=str, help="Palavra-chave para busca")
    parser.add_argument("--limit", type=int, default=10, help="Limite de skills por lote")
    parser.add_argument("--all", action="store_true", help="Baixar todas as skills")
    parser.add_argument("--download", action="store_true", help="Tentar baixar os arquivos SKILL.md")
    
    args = parser.parse_args()
    if not args.keyword and not args.all:
        print("Erro: Use --keyword ou --all.")
        sys.exit(1)
        
    results = get_skills(keyword=args.keyword, limit=args.limit, all_mode=args.all, download=args.download)
    
    with open("skills_found.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)
    print(f"\nFinalizado! {len(results)} skills processadas.")

if __name__ == "__main__":
    main()
