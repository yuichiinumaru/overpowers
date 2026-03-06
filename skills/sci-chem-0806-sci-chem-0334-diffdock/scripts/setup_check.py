import sys

def main():
    print("Checking DiffDock environment setup...")

    issues = False
    try:
        import torch
        print(f"✅ PyTorch installed: {torch.__version__}")
        if torch.cuda.is_available():
            print(f"✅ CUDA available: {torch.version.cuda}")
        else:
            print("⚠️ CUDA not available. Inference will be slow.")
    except ImportError:
        print("❌ PyTorch not installed")
        issues = True

    try:
        import torch_geometric
        print(f"✅ PyTorch Geometric installed: {torch_geometric.__version__}")
    except ImportError:
        print("❌ PyTorch Geometric not installed")
        issues = True

    try:
        import rdkit
        print(f"✅ RDKit installed: {rdkit.__version__}")
    except ImportError:
        print("❌ RDKit not installed")
        issues = True

    if issues:
        print("\nEnvironment has issues. Please refer to DiffDock installation instructions.")
        sys.exit(1)
    else:
        print("\nEnvironment appears ready for basic inference.")

if __name__ == "__main__":
    main()
