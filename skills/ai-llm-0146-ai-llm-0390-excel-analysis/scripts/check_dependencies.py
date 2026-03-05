def check_deps():
    try:
        import pandas as pd
        print(f"✅ pandas {pd.__version__} is installed.")
    except ImportError:
        print("❌ pandas is not installed.")

    try:
        import openpyxl
        print("✅ openpyxl is installed.")
    except ImportError:
        print("❌ openpyxl is not installed.")

if __name__ == "__main__":
    check_deps()
