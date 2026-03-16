#!/bin/bash
# Install dependencies for semantic similarity detection
# Uses Qwen3-Embedding-0.6B (lightweight, works great on RTX 3070 8GB)
# Uses UV for fast installation (10-100x faster than pip)

echo "🔧 Installing semantic similarity detection dependencies with UV..."
echo ""

# Check if UV is installed
if ! command -v uv &> /dev/null; then
    echo "⚠️  UV not found. Installing UV..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.local/bin/env 2>/dev/null || true
    export PATH="$HOME/.local/bin:$PATH"
fi

# Verify UV installation
if ! command -v uv &> /dev/null; then
    echo "❌ Failed to install UV. Please install manually:"
    echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

echo "✅ UV version: $(uv --version)"
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 not found. Please install Python 3.8+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✅ $PYTHON_VERSION"
echo ""

# Check if CUDA is available (optional but recommended)
if command -v nvidia-smi &> /dev/null; then
    echo "✅ NVIDIA GPU detected"
    nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
    echo "💡 Will use GPU acceleration for embeddings"
    echo ""
else
    echo "⚠️  No NVIDIA GPU detected"
    echo "💡 Will use CPU (slower but still works)"
    echo ""
fi

# Create requirements file
cat > /tmp/requirements-similarity.txt << EOF
# Semantic Similarity Detection Requirements
torch>=2.0.0
sentence-transformers>=2.2.0
transformers>=4.30.0
EOF

# Install with UV (much faster than pip)
echo "📦 Installing dependencies with UV (this is fast...)..."
if command -v nvidia-smi &> /dev/null; then
    # GPU version
    uv pip install --system torch --index-url https://download.pytorch.org/whl/cu118
else
    # CPU version
    uv pip install --system torch
fi

# Install other dependencies
uv pip install --system -r /tmp/requirements-similarity.txt

# Clean up
rm /tmp/requirements-similarity.txt

# Download the model (optional - will download on first run anyway)
echo ""
echo "🤖 Downloading Qwen3-Embedding-0.6B model..."
echo "💡 This is ~500MB and may take a few minutes..."
python3 -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('Qwen/Qwen3-Embedding-0.6B', trust_remote_code=True)"

echo ""
echo "✅ Installation complete!"
echo ""
echo "🚀 Run the detector with:"
echo "   python3 scripts/detect-similar-skills.py"
echo ""
echo "📊 The model will detect similar skills across different languages!"
echo ""
echo "💡 Pro tip: UV is 10-100x faster than pip. You're welcome!"
