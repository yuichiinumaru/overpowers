import os

def audit_dx():
    checks = {
        "README.md": os.path.exists("README.md"),
        ".env.example": os.path.exists(".env.example"),
        "package.json": os.path.exists("package.json"),
        "Makefile": os.path.exists("Makefile"),
        "docker-compose.yml": os.path.exists("docker-compose.yml"),
        "scripts/setup.sh": os.path.exists("scripts/setup.sh"),
    }
    
    print("DX Audit Results:")
    for item, exists in checks.items():
        status = "✅ Found" if exists else "❌ Missing"
        print(f"- {item}: {status}")

if __name__ == "__main__":
    audit_dx()
