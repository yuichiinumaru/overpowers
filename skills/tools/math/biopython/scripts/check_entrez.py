import sys
from Bio import Entrez

def check_entrez(email):
    Entrez.email = email
    print(f"🔍 Testing Entrez connection with email: {email}...")
    try:
        handle = Entrez.einfo()
        result = Entrez.read(handle)
        handle.close()
        print("✅ Entrez connection successful!")
        print(f"Available databases: {', '.join(result['DbList'][:10])}...")
        return True
    except Exception as e:
        print(f"❌ Entrez connection failed: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_entrez.py <your_email>")
        sys.exit(1)
    
    email = sys.argv[1]
    if not check_entrez(email):
        sys.exit(1)

if __name__ == "__main__":
    main()
