#!/usr/bin/env python3
"""
GitHub Repository Cloner for Batch Extraction
Clones repositories and extracts skills/agents/workflows/hooks to staging.
"""

import subprocess
import shutil
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List

# Configuration
REPO_ROOT = Path("/home/sephiroth/Work/overpowers")
TEMP_DIR = REPO_ROOT / "temp" / "extract-github"
STAGING_DIR = REPO_ROOT / ".archive/staging"


def clone_repo(repo_url: str, target_dir: Path) -> bool:
    """Clone a GitHub repository (shallow clone for speed)."""
    print(f"📥 Cloning {repo_url}...")
    
    try:
        # Shallow clone (only latest commit)
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, str(target_dir)],
            check=True,
            capture_output=True,
            timeout=300
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"   ❌ Clone failed: {e.stderr.decode() if e.stderr else str(e)}")
        return False
    except subprocess.TimeoutExpired:
        print(f"   ❌ Clone timed out (5 min limit)")
        return False


def detect_repo_type(repo_dir: Path) -> str:
    """Detect if repo is direct skills or awesome list."""
    # Check for direct skill structure
    if (repo_dir / "skills").exists() or (repo_dir / "SKILL.md").exists():
        return "direct"
    
    # Check for awesome list (README with GitHub URLs)
    readme = repo_dir / "README.md"
    if readme.exists():
        content = readme.read_text()
        if "github.com" in content and ("skill" in content.lower() or "agent" in content.lower()):
            return "awesome-list"
    
    # Check for agents/workflows/hooks directories
    for subdir in ["agents", "workflows", "hooks"]:
        if (repo_dir / subdir).exists():
            return "direct"
    
    return "unknown"


def extract_assets(repo_dir: Path, repo_type: str, repo_name: str) -> Dict:
    """Extract skills/agents/workflows/hooks from cloned repo."""
    result = {
        'repo': repo_name,
        'type': repo_type,
        'extracted': {
            'skills': [],
            'agents': [],
            'workflows': [],
            'hooks': []
        },
        'errors': []
    }
    
    if repo_type == "direct":
        # Extract from direct structure
        for asset_type in ['skills', 'agents', 'workflows', 'hooks']:
            source_dir = repo_dir / asset_type
            if not source_dir.exists():
                continue
            
            staging_subdir = STAGING_DIR / asset_type
            staging_subdir.mkdir(parents=True, exist_ok=True)
            
            for item in source_dir.iterdir():
                if item.is_file() and item.suffix == '.md':
                    # Copy to staging
                    dest = staging_subdir / f"{repo_name}_{item.name}"
                    shutil.copy2(item, dest)
                    result['extracted'][asset_type].append(str(dest))
                
                elif item.is_dir() and (item / "SKILL.md").exists():
                    # Skill directory - copy entire folder content
                    for skill_file in item.rglob("*"):
                        if skill_file.is_file():
                            dest_name = f"{repo_name}_{item.name}_{skill_file.name}"
                            dest = staging_subdir / dest_name
                            shutil.copy2(skill_file, dest)
                            result['extracted'][asset_type].append(str(dest))
    
    elif repo_type == "awesome-list":
        # Parse README for GitHub URLs and clone those
        readme = repo_dir / "README.md"
        if not readme.exists():
            result['errors'].append("README.md not found in awesome list")
            return result
        
        content = readme.read_text()
        
        # Extract GitHub URLs
        import re
        github_urls = re.findall(r'https://github\.com/[\w-]+/[\w-]+', content)
        
        print(f"   📋 Found {len(github_urls)} GitHub URLs in awesome list")
        
        # Clone each referenced repo
        for url in github_urls[:10]:  # Limit to first 10 to avoid timeout
            sub_repo_name = url.split('/')[-1]
            sub_target = TEMP_DIR / f"sub_{sub_repo_name}"
            
            if clone_repo(url, sub_target):
                sub_type = detect_repo_type(sub_target)
                sub_result = extract_assets(sub_target, sub_type, f"{repo_name}_{sub_repo_name}")
                
                # Merge results
                for asset_type in ['skills', 'agents', 'workflows', 'hooks']:
                    result['extracted'][asset_type].extend(sub_result['extracted'][asset_type])
                
                # Cleanup sub-repo
                shutil.rmtree(sub_target, ignore_errors=True)
    
    return result


def clone_and_extract(repo_urls: List[str]) -> Dict:
    """Main function: clone repos and extract assets."""
    print(f"\n{'='*60}")
    print(f"GITHUB CLONE & EXTRACT")
    print(f"{'='*60}\n")
    
    # Create temp directory
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    
    all_results = {
        'timestamp': datetime.now().isoformat(),
        'repos': [],
        'summary': {
            'total_repos': len(repo_urls),
            'successful_clones': 0,
            'failed_clones': 0,
            'total_extracted': {
                'skills': 0,
                'agents': 0,
                'workflows': 0,
                'hooks': 0
            }
        }
    }
    
    for i, repo_url in enumerate(repo_urls, 1):
        print(f"\n[{i}/{len(repo_urls)}] Processing {repo_url}")
        
        repo_name = repo_url.split('/')[-1].replace('.git', '')
        target_dir = TEMP_DIR / repo_name
        
        # Clone
        if not clone_repo(repo_url, target_dir):
            all_results['repos'].append({
                'url': repo_url,
                'name': repo_name,
                'status': 'clone_failed'
            })
            all_results['summary']['failed_clones'] += 1
            continue
        
        # Detect type
        repo_type = detect_repo_type(target_dir)
        print(f"   📊 Repo type: {repo_type}")
        
        # Extract
        extract_result = extract_assets(target_dir, repo_type, repo_name)
        
        # Cleanup clone
        shutil.rmtree(target_dir, ignore_errors=True)
        
        # Record result
        all_results['repos'].append({
            'url': repo_url,
            'name': repo_name,
            'type': repo_type,
            'status': 'extracted',
            'extracted': extract_result['extracted']
        })
        all_results['summary']['successful_clones'] += 1
        
        for asset_type in ['skills', 'agents', 'workflows', 'hooks']:
            all_results['summary']['total_extracted'][asset_type] += len(extract_result['extracted'][asset_type])
    
    # Cleanup temp
    shutil.rmtree(TEMP_DIR, ignore_errors=True)
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"EXTRACTION SUMMARY")
    print(f"{'='*60}")
    print(f"  Repos processed:     {all_results['summary']['total_repos']}")
    print(f"  Successful clones:   {all_results['summary']['successful_clones']}")
    print(f"  Failed clones:       {all_results['summary']['failed_clones']}")
    print(f"\n  Extracted to staging:")
    for asset_type, count in all_results['summary']['total_extracted'].items():
        print(f"    - {asset_type.capitalize()}: {count}")
    print(f"{'='*60}\n")
    
    return all_results


def main():
    """Main entry point."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 clone-github-repos.py <repo_url1> [repo_url2] ...")
        print("   or: python3 clone-github-repos.py --file <urls_file.txt>")
        return 1
    
    # Parse arguments
    repo_urls = []
    
    if sys.argv[1] == '--file':
        # Read from file
        urls_file = Path(sys.argv[2])
        if urls_file.exists():
            repo_urls = [line.strip() for line in urls_file.read_text().split('\n') if line.strip() and not line.startswith('#')]
        else:
            print(f"❌ File not found: {urls_file}")
            return 1
    else:
        # Direct URLs
        repo_urls = sys.argv[1:]
    
    print(f"📋 Processing {len(repo_urls)} repositories...\n")
    
    # Clone and extract
    result = clone_and_extract(repo_urls)
    
    # Save result log
    log_file = REPO_ROOT / ".docs" / "github-extraction-log.json"
    with open(log_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print(f"📝 Extraction log saved to: {log_file}")
    
    return 0 if result['summary']['failed_clones'] == 0 else 1


if __name__ == '__main__':
    exit(main())
