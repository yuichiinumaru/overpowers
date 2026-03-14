---
name: legal-software-copyright-cn
version: 1.0.0
description: Material generator for Chinese software copyright registration. Automatically generates application forms, source code identification materials (with syntax highlighting), and user manuals in PDF format.
tags: [legal, copyright, registration, china, documentation, pdf-generation]
category: legal
---

# 软著申请材料生成 (Software Copyright Material Generator)

## 依赖

确保已安装：`pip install reportlab pygments`

## 工作流程

### 阶段一：收集基本信息

通过对话逐步收集必填字段（软件全称、版本号、硬件环境、运行平台、编程语言等）。详细字段见 `references/fields.md`。

### 阶段二：信息确认

用户确认无误后，将全部信息保存为 `software_info.json`。

### 阶段三：生成程序鉴别材料

运行脚本生成带语法高亮的源代码PDF：

```bash
python scripts/generate_source_pdf.py <源代码目录> --name "软件全称" --version "V1.0" -o 程序鉴别材料.pdf
```

### 阶段四：生成文档鉴别材料

**方式一（推荐）：从配置自动生成用户手册**

```bash
python scripts/generate_doc_pdf.py --config software_info.json -o 文档鉴别材料.pdf
```

**方式二：从已有文档转换**

```bash
python scripts/generate_doc_pdf.py --input manual.txt --name "软件名" --version "V1.0" --author "权利人" -o 文档鉴别材料.pdf
```

### 阶段五：材料清单确认

生成完毕后，输出最终材料清单 (software_info.json, 程序鉴别材料.pdf, 文档鉴别材料.pdf).

## 注意事项

- 所有生成的PDF使用系统中文字体
- 程序鉴别材料使用 Pygments 实现语法高亮
- 源代码自动跳过 node_modules、.git 等目录
