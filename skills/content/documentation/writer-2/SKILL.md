---
name: financial-content-writer
description: Finance and tax audit content generator - quickly generate professional finance and tax public account articles, supporting multiple article types and topics.
tags: [finance, tax, audit, content-generation, wechat, article-writing]
version: "1.0.0"
---

# Finance and Tax Audit Content Generator

## Trigger Methods

Activates when user says similar to:
- "Help me write a finance article"
- "Generate an audit article about XX"
- "I want to write public account content"
- "Write a policy interpretation"
- Commands starting with `/fin`

---

## Feature Overview

| Feature | Command | Description |
|------|------|------|
| **Interactive Mode** | `/fin` | Enter interactive content generation dialogue |
| **Generate Article** | `/fin-article {topic}` | Generate finance/audit article (public account format) |
| **Full Article** | `/fin-full {topic}` | Generate full version article |
| **Case Analysis** | `/fin-case {topic}` | Generate case analysis articles |
| **Policy Interpretation** | `/fin-policy {topic}` | Generate policy interpretation articles |
| **Risk Warning** | `/fin-risk {topic}` | Generate risk warning articles |
| **Experience Sharing** | `/fin-share {topic}` | Generate experience sharing articles |
| **Practical Guide** | `/fin-guide {topic}` | Generate practical guide articles |
| **Technical Tutorial** | `/fin-tutorial {topic}` | Generate technical tutorial articles |
| **Industry Insight** | `/fin-insight {topic}` | Generate industry insight articles |
| **View Topics** | `/fin-topics` | View all popular article topics |
| **View by Domain** | `/fin-audit` `/fin-finance` `/fin-tax` etc. | View popular topics in specific domain |
| **Generate Outline** | `/fin-outline {topic}` | Generate article outline |
| **Generate Titles** | `/fin-titles {topic}` | Generate article title options |
| **Generate Images** | `/fin-images {article_path}` | Generate accompanying images for finance articles |

---

## Supported Article Types

| Type | Use Case | Example Topics |
|------|----------|----------------|
| Case Analysis | Real case interpretation | "Listed company financial fraud case" |
| Policy Interpretation | New policy impact analysis | "New Company Law Interpretation" |
| Risk Warning | Compliance risk alert | "Golden Tax Phase IV risk points" |
| Experience Sharing | Practical experience summary | "Audit newcomer pitfall avoidance guide" |
| Practical Guide | Operational guide | "Small company internal control system" |
| Technical Tutorial | Professional skill teaching | "Excel financial modeling" |
| Industry Insight | Trend analysis | "2024 Finance industry trends" |

---

## Supported Professional Domains

| Domain | Command | Popular Topic Examples |
|------|------|------------------------|
| Audit | `/fin-audit` | Financial fraud, internal control audit, due diligence |
| Finance | `/fin-finance` | Financial statement analysis, cost control, budget management |
| Tax | `/fin-tax` | Individual tax settlement, tax planning, invoice management |
| Policy | `/fin-policy-topics` | Company Law, Tax Law, Accounting Standards |
| Technology | `/fin-tech` | Excel, Python, Financial Systems |

---

## Editorial Review Workflow

Complete multi-role review process:

| Role | Command | Review Perspective |
|------|------|-------------------|
| **Full Process** | `/fin-review {topic}` | Full process review |
| **Architect** | `/fin-review-architect` | Traffic + Conversion |
| **Lead Writer** | `/fin-review-writer` | Structure + Depth |
| **Acid Editor** | `/fin-review-acid` | Error finding + Quality |
| **Ghost Writer** | `/fin-review-ghost` | Expression + Readability |
| **Packager** | `/fin-review-pack` | Viral + Monetization |

---

## Image Generation

| Command | Description |
|------|------|
| `/fin-images {path}` | Finance article images |
| `/fin-images-tax {path}` | Tax article images |
| `/fin-images-audit {path}` | Audit article images |
| `/fin-images-finance {path}` | Finance article images |
| `/fin-images-policy {path}` | Policy interpretation images |
| `/fin-images-risk {path}` | Risk warning images |

---

## Usage Flow

### Method 1: Direct Article Generation

```
User: /fin-article Small company financial chaos
```

### Method 2: View Popular Topics First

```
User: /fin-topics
→ Get popular topic list

User: /fin-article Impact of new Company Law implementation
```

### Method 3: Complete Creation Flow

```
1. /fin-outline {topic}      # Generate outline
2. /fin-titles {topic}       # Generate title options
3. /fin-article {topic}      # Generate article
4. /fin-images {article path}   # Generate images
```

---

## Article Format Features

- **Public Account Format**: Adapted for WeChat public account editor
- **Professionally Accurate**: Based on finance and tax professional knowledge base
- **Practical Orientation**: Focus on practical operations and actionable advice
- **Diverse Styles**: Supports serious professional content and fun popular science

---

## File Structure

```
finance-content-writer/
├── SKILL.md                           # This file
├── finance-content-skill.json         # Command configuration
├── finance-content-generator.js       # Content generation script
├── finance-image-generator.cjs        # Image generation script
└── editorial-workflow.js              # Editorial review script
```
