#!/usr/bin/env python3
"""
Detect Environment Script
Auto-detect project environment dan tech stack.
Supports Multi-OS Profiles (Windows/Linux/macOS) to prevent config overwrites.

Usage:
    python scripts/detect-environment.py
"""

import json
import os
import platform
import socket
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


def detect_environment() -> Dict:
    """Detect current environment details and merge with existing profiles"""

    # Find project root (scripts are now in .agent/scripts/)
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent.parent  # .agent/scripts -> .agent -> project_root

    # OUTPUT PATH
    output_file = project_root / '.agent' / 'context' / 'environment.json'

    # 1. LOAD EXISTING DATA (for persistence)
    existing_data = {}
    if output_file.exists():
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except:
            pass

    # 2. DETECT CURRENT OS
    system = platform.system().lower()
    current_os_type = {
        'windows': 'windows',
        'linux': 'linux',
        'darwin': 'macos'
    }.get(system, 'unknown')

    # 3. DETECT NEW DETAILS (Current OS)
    username = os.getenv('USERNAME') or os.getenv('USER') or 'unknown'
    user_home = str(Path.home())

    # Shell detection
    if current_os_type == 'windows':
        shell = 'powershell'
    else:
        shell = os.getenv('SHELL', 'bash').split('/')[-1]

    web_root = detect_web_root()
    tech_stack = detect_tech_stack(project_root)
    databases = detect_databases(project_root)

    current_profile_data = {
        'detected': datetime.now().isoformat(),
        'os': current_os_type,
        'username': username,
        'userHome': user_home,
        'hostname': socket.gethostname(),
        'projectRoot': str(project_root),
        'webRoot': web_root,
        'shell': shell,
        'techStack': tech_stack,
        'databases': databases,
        'python': platform.python_version(),
        'architecture': platform.machine()
    }

    # 4. MERGE / MIGRATE LOGIC
    # Initialize new structure
    new_data = {
        "last_updated": datetime.now().isoformat(),
        "active_profile": current_os_type,
        "profiles": {}
    }

    # Migration: Check if existing data is "legacy flat format"
    if existing_data and 'profiles' not in existing_data:
        # It's a flat file. Check which OS it was.
        old_os = existing_data.get('os', 'unknown')
        if old_os != 'unknown':
            new_data['profiles'][old_os] = existing_data
            print(f"📦 Migrated legacy {old_os} config to profile.")

    elif existing_data and 'profiles' in existing_data:
        # It's already new format. Keep existing profiles.
        new_data['profiles'] = existing_data['profiles']

    # Update/Overwrite CURRENT OS profile
    new_data['profiles'][current_os_type] = current_profile_data

    return new_data


def detect_web_root() -> Optional[str]:
    """Detect web server root directory"""
    possible_roots = [
        Path('C:/laragon/www'),
        Path('F:/laragon/www'),
        Path('D:/laragon/www'),
        Path('C:/xampp/htdocs'),
        Path('/var/www/html'),
        Path('/usr/local/var/www'),
        Path.home() / 'www'
    ]

    for root in possible_roots:
        if root.exists():
            return str(root)

    return None


def detect_tech_stack(root: Path) -> Dict[str, List[str]]:
    """Detect project tech stack"""
    stack = {
        'backend': [],
        'frontend': [],
        'database': [],
        'tools': []
    }

    # PHP Detection
    if (root / 'composer.json').exists():
        stack['backend'].append('php')
        try:
            with open(root / 'composer.json', encoding='utf-8') as f:
                data = json.load(f)
                require = data.get('require', {})
                if 'laravel/framework' in require:
                    stack['backend'].append('laravel')
                elif 'yiisoft/yii' in require or 'yiisoft/yii2' in require:
                    stack['backend'].append('yii')
                elif 'symfony/framework-bundle' in require:
                    stack['backend'].append('symfony')
        except:
            pass

    # Node.js Detection
    if (root / 'package.json').exists():
        stack['backend'].append('nodejs')
        try:
            with open(root / 'package.json', encoding='utf-8') as f:
                data = json.load(f)
                deps = {**data.get('dependencies', {}), **data.get('devDependencies', {})}
                if 'express' in deps:
                    stack['backend'].append('express')
                if 'fastify' in deps:
                    stack['backend'].append('fastify')
                if 'next' in deps:
                    stack['frontend'].append('nextjs')
                if 'react' in deps:
                    stack['frontend'].append('react')
                if 'vue' in deps:
                    stack['frontend'].append('vue')
                if 'angular' in deps or '@angular/core' in deps:
                    stack['frontend'].append('angular')
        except:
            pass

    # Python Detection
    if (root / 'requirements.txt').exists() or (root / 'Pipfile').exists() or (root / 'pyproject.toml').exists():
        stack['backend'].append('python')
        # Check for frameworks
        for req_file in ['requirements.txt', 'Pipfile']:
            req_path = root / req_file
            if req_path.exists():
                try:
                    content = req_path.read_text(encoding='utf-8').lower()
                    if 'django' in content:
                        stack['backend'].append('django')
                    if 'flask' in content:
                        stack['backend'].append('flask')
                    if 'fastapi' in content:
                        stack['backend'].append('fastapi')
                except:
                    pass

    # Go Detection
    if (root / 'go.mod').exists():
        stack['backend'].append('go')

    # Rust Detection
    if (root / 'Cargo.toml').exists():
        stack['backend'].append('rust')

    # Java/Kotlin Detection
    if (root / 'pom.xml').exists():
        stack['backend'].append('java')
        stack['backend'].append('maven')
    if (root / 'build.gradle').exists() or (root / 'build.gradle.kts').exists():
        stack['backend'].append('java')
        stack['backend'].append('gradle')

    # .NET Detection
    if list(root.glob('*.csproj')) or list(root.glob('*.fsproj')):
        stack['backend'].append('dotnet')
    if (root / '*.sln').exists() or list(root.glob('*.sln')):
        stack['backend'].append('dotnet')

    # Ruby Detection
    if (root / 'Gemfile').exists():
        stack['backend'].append('ruby')
        try:
            content = (root / 'Gemfile').read_text(encoding='utf-8').lower()
            if 'rails' in content:
                stack['backend'].append('rails')
        except:
            pass

    # Tools Detection
    if (root / '.git').exists():
        stack['tools'].append('git')
    if (root / 'docker-compose.yml').exists() or (root / 'docker-compose.yaml').exists():
        stack['tools'].append('docker')
    if (root / 'Dockerfile').exists():
        stack['tools'].append('docker')
    if (root / '.github' / 'workflows').exists():
        stack['tools'].append('github-actions')
    if (root / 'Makefile').exists():
        stack['tools'].append('make')

    # Check for Laragon
    if detect_web_root() and 'laragon' in detect_web_root().lower():
        stack['tools'].append('laragon')

    # Remove duplicates while preserving order
    for key in stack:
        stack[key] = list(dict.fromkeys(stack[key]))

    return stack


def detect_databases(root: Path) -> Dict:
    """Detect database configurations"""
    databases = {}

    # Check .env file
    env_file = root / '.env'
    if env_file.exists():
        try:
            content = env_file.read_text(encoding='utf-8').lower()

            if 'mysql' in content or '3306' in content:
                databases['mysql'] = {
                    'host': '127.0.0.1',
                    'port': 3306
                }

            if 'oracle' in content or '1521' in content:
                databases['oracle'] = {
                    'host': 'localhost',
                    'port': 1521
                }

            if 'postgresql' in content or '5432' in content:
                databases['postgresql'] = {
                    'host': 'localhost',
                    'port': 5432
                }
        except:
            pass

    # Default databases based on common setups
    if not databases:
        databases = {
            'mysql': {'host': '127.0.0.1', 'port': 3306},
            'oracle': {'host': 'localhost', 'port': 1521}
        }

    return databases


def save_environment():
    """Save environment to JSON file with profiling support"""
    env_data = detect_environment()

    # Output path - relative from script location (.agent/scripts/)
    script_path = Path(__file__).resolve()
    project_root = script_path.parent.parent.parent  # .agent/scripts -> .agent -> project_root
    output_file = project_root / '.agent' / 'context' / 'environment.json'
    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Save
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(env_data, f, indent=2, ensure_ascii=False)

    # Print summary
    current_profile = env_data['active_profile']
    details = env_data['profiles'][current_profile]

    print(f"✅ Environment detected!")
    print(f"   Mode: Profiled ({current_profile})")
    print(f"   OS: {details['os']}")
    print(f"   User: {details['username']}")
    print(f"   Project: {details['projectRoot']}")
    print(f"   Profiles Stored: {', '.join(env_data['profiles'].keys())}")
    print(f"   Saved to: {output_file}")

    return env_data


if __name__ == '__main__':
    save_environment()
