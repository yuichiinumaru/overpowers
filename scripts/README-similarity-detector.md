# Semantic Similarity Detector for Skills

Detects similar skills across different languages using AI embeddings.

## 🎯 What It Does

This tool scans all skills in the repository and identifies:
- **Exact duplicates** (same content, different locations)
- **Translations** (same skill in different languages)
- **Similar functionality** (skills that do similar things)

## 🚀 Quick Start

### Option 1: Automated Installation (Recommended)

```bash
# Make script executable and run installation
chmod +x scripts/install-similarity-detector.sh
./scripts/install-similarity-detector.sh
```

This will:
1. Install PyTorch with CUDA support (uses your RTX 3070)
2. Install sentence-transformers
3. Download the Qwen3-Embedding-0.6B model (~500MB)

### Option 2: Manual Installation

```bash
# Install dependencies
pip3 install sentence-transformers transformers torch

# Run the detector
python3 scripts/detect-similar-skills.py
```

## 🤖 Model Information

**Model**: Qwen3-Embedding-0.6B
- **Size**: ~500MB
- **VRAM Usage**: ~1-2GB on GPU
- **Languages**: Multilingual (excellent for Chinese/English/Russian detection)
- **Speed**: ~100-200 skills/second on RTX 3070
- **Accuracy**: High precision for cross-language similarity

### Why This Model?

1. **Lightweight**: Only 0.6B parameters, fits easily on 8GB VRAM
2. **Multilingual**: Trained on multiple languages, perfect for detecting translations
3. **Fast**: Quick inference on GPU
4. **Accurate**: State-of-the-art embedding quality

## 📊 Output Files

After running, you'll get:

### 1. Markdown Report
`.docs/tasks/planning/similar-skills-report.md`

Contains:
- Summary statistics
- High similarity pairs (≥80%)
- Medium similarity pairs (60-80%)
- Translation clusters
- Recommendations

### 2. JSON Data
`.docs/tasks/planning/similar-skills-data.json`

Machine-readable data for programmatic access.

## 📈 Understanding Results

### Similarity Scores

| Score | Meaning | Action |
|-------|---------|--------|
| **100%** | Exact duplicate | Merge or delete one |
| **80-99%** | Very similar (likely translation) | Review and consolidate |
| **60-80%** | Related functionality | Check if should be merged |
| **30-60%** | May be related | Manual review |

### Example Output

```markdown
### 1. Similarity: 95.2%

**Skill 1**: `skills/fortune-telling-cn/SKILL.md`
  - Languages Detected: Chinese (60%)
  - Preview: 算命工具，支持八字、紫微斗数...

**Skill 2**: `skills/fortune-telling/SKILL.md`
  - Languages Detected: English
  - Preview: Fortune telling tool with Bazi, Ziwei...

**Scores**: Cosine=92.1%, Keywords=85.3%
```

This indicates the Chinese skill is likely a translation of the English one!

## 🔧 Advanced Usage

### Adjust Similarity Threshold

```python
# In detect-similar-skills.py, line ~280
similar_pairs = detector.find_similar_skills(
    threshold=0.6,           # Minimum similarity score
    min_keyword_similarity=0.3  # Minimum keyword overlap
)
```

### Use CPU Only

```python
# Line ~141
self.model = SentenceTransformer(
    MODEL_NAME,
    trust_remote_code=True,
    device='cpu'  # Force CPU usage
)
```

### Batch Size for Large Datasets

```python
# Line ~169
batch_size = 32  # Reduce if out of memory
```

## 🐛 Troubleshooting

### Out of Memory

If you get CUDA out of memory:
1. Reduce batch_size to 16 or 8
2. Close other GPU applications
3. Use CPU mode (slower but works)

### Model Download Fails

If network is slow:
```bash
# Download manually
huggingface-cli download Qwen/Qwen3-Embedding-0.6B
```

### No GPU Detected

Check NVIDIA drivers:
```bash
nvidia-smi
```

If not showing, install/update drivers.

## 📝 Integration with Translation Workflow

After detecting similar skills:

1. **Review the report**: Check high-similarity pairs
2. **Identify translations**: Skills with >80% similarity in different languages
3. **Batch translate**: Use the translation batches (task 0510-*)
4. **Consolidate**: Merge duplicate functionality
5. **Archive**: Move old versions to `.archive/`

## 💡 Tips

1. **Run before translation**: Detect duplicates first to avoid translating redundant skills
2. **Check clusters**: Translation clusters show groups of related skills
3. **Use keyword fallback**: If model fails, script still works with keyword-only mode
4. **GPU recommended**: 10x faster on RTX 3070 vs CPU

## 📚 References

- [Qwen3-Embedding-0.6B on HuggingFace](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)
- [Sentence Transformers Documentation](https://www.sbert.net/)
- [CSDN Guide (Chinese)](https://blog.csdn.net/weixin_42124497/article/details/157629234)

---

*Last updated: 2026-03-16*
