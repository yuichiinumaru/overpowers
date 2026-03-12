#!/bin/bash
# Setup Lemon AI Agent locally

echo "🍋 Setting up Lemon AI..."

# 1. Clone repository
if [ ! -d "lemon-ai" ]; then
    echo "📥 Cloning repository..."
    git clone https://github.com/lemon-ai/lemon-ai.git
    cd lemon-ai
else
    echo "⏭️  Lemon AI already cloned, skipping."
    cd lemon-ai
fi

# 2. Create virtual environment
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
fi

# 3. Install dependencies
echo "📦 Installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

# 4. Configure environment
if [ ! -f ".env" ]; then
    echo "⚙️ Creating template .env file..."
    cat > .env << EOF
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
# Local LLM Backend (Ollama)
LLM_BACKEND_URL=http://localhost:11434
EOF
    echo "✅ Template .env created. Please update with your keys."
fi

echo ""
echo "✨ Lemon AI setup complete! Run 'python main.py' to start."
