---
name: safety-sec-zipcracker
description: 高性能多并发 ZIP 密码破解工具。支持伪加密修复、字典攻击、CRC32 碰撞和掩码攻击。专为 Agent 静默执行优化。
tags: [security, password-cracking, zip, safety]
version: 1.0.0
---

# ZipCracker Skill - ZIP密码破解工具

ZipCracker Skill 是基于Hx0战队开发的ZipCracker项目改造的OpenClaw技能。它是一款高性能的多并发ZIP密码破解工具，支持多种破解方式，包括伪加密检测修复、字典攻击、CRC32碰撞和掩码攻击。**本版本已针对 OpenClaw Agent 深度优化，支持后台静默执行与标准 JSON 输出。**

## 功能特性

### ✅ 核心功能
1. **伪加密检测与修复** - 自动识别并修复伪加密ZIP文件
2. **字典攻击** - 内置6000+常用密码字典，支持自定义字典
3. **CRC32碰撞** - 针对小于6字节的文件进行CRC碰撞破解
4. **掩码攻击** - 支持已知密码结构的智能破解
5. **AES加密支持** - 支持AES加密的ZIP文件破解

### ✅ 技术特性
- 多线程并发，自动调整最优线程数
- 智能识别文件类型和加密方式
- 自动提取破解成功的文件
- **Agent 静默模式**：剥离阻塞交互，专为 AI 大模型异步调用设计

## 安装依赖与注册

在 OpenClaw 的 `skills` 目录下直接运行安装脚本，系统会自动配置 Python 依赖并向 ClawHub 注册：

```bash
chmod +x install.sh
./install.sh

```

## 🤖 OpenClaw 智能助手调用示例

你可以直接通过自然语言让 OpenClaw 帮你执行破解：

* “帮我破解一下桌面的 `test.zip`，使用内置字典。”
* “这个 `secret.zip` 的密码应该是 4 位纯数字，用掩码帮我爆破一下，解压到 `output` 文件夹。”
* “检测一下 `flag.zip` 是不是伪加密，是的话直接帮我修复提取。”

## CLI 手动使用方法

如果你想在终端中手动使用，请参考以下基础命令：

```bash
# 检查伪加密并自动修复
python3 zipcracker.py test.zip

# 使用自定义字典破解
python3 zipcracker.py encrypted.zip custom_dict.txt

# 掩码攻击（已知密码结构）
python3 zipcracker.py encrypted.zip -m '?uali?s?d?d?d'

```

### 掩码占位符规则

| 占位符 | 代表的字符集 |
| --- | --- |
| `?d` | 数字 (0-9) |
| `?l` | 小写字母 (a-z) |
| `?u` | 大写字母 (A-Z) |
| `?s` | 特殊符号 |
| `??` | 问号 `?` 自身 |

## 参数说明

```
python3 zipcracker.py <ZIP文件> [字典文件/目录] [-o 输出目录] [-m 掩码] [--agent]

```

* `<ZIP文件>`: 要破解的ZIP文件路径
* `[字典文件/目录]`: 可选的自定义字典文件或目录
* `-o, --out`: 指定输出目录（默认: unzipped_files）
* `-m, --mask`: 使用掩码攻击，指定密码结构
* `--agent`: **(OpenClaw 专属)** 开启静默模式，跳过所有手动确认 (如 CRC 碰撞提示)，并输出标准 JSON 供大模型解析。

## 安全与法律声明

⚠️ **重要提醒** ⚠️

1. **合法用途**: 本工具仅用于安全测试、CTF比赛、密码恢复等合法用途
2. **授权使用**: 仅在拥有合法权限的情况下使用
3. **责任自负**: 用户滥用造成的一切后果与作者无关
4. **遵守法律**: 使用者请务必遵守当地法律法规
5. **学习交流**: 本程序不得用于商业用途，仅限学习交流

## 开发者

* **原作者**: Hx0战队
* **Skill适配**: Hx0工作室智能助手
* **许可证**: 仅限学习交流使用
