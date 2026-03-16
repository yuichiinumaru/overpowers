---
name: jax-skill-security-scanner
description: "OpenClaw技能安全扫描插件，包含敏感操作检测和木马/后门检测功能"
metadata:
  openclaw:
    category: "security"
    tags: ['security', 'audit', 'monitoring']
    version: "1.0.0"
---

# 技能安全扫描器

OpenClaw技能安全扫描插件，提供完整的技能安全扫描功能，包括敏感操作检测和木马/后门检测。

## 功能特性

### 🔍 敏感操作检测
- 扫描SKILL.md文件中的敏感关键词
- 检查package.json中的危险脚本
- 分析JavaScript/TypeScript代码文件
- 自动评估风险等级（高/中/低）

### 🦠 木马/后门检测
- 网络通信后门检测（net, http, ws, socket.io等）
- 文件系统恶意操作检测（fs模块危险函数）
- 进程控制系统检测（child_process, exec, spawn等）
- 数据外传加密检测（crypto, Buffer, base64编码）
- 代码混淆隐藏检测（eval, Function构造器等）
- 高风险组合模式识别

### 📊 报告生成
- 文本格式报告
- Markdown格式报告
- JSON格式报告
- 风险统计摘要
- 木马检测摘要
- 安全建议

## 安装

### 作为npm包安装

```bash
# 全局安装命令行工具
npm install -g @jax-npm/skill-security-scanner

# 或作为依赖安装
npm install @jax-npm/skill-security-scanner
```

### 作为OpenClaw插件安装

```bash
# 从npm安装
openclaw-cn plugins add @jax-npm/skill-security-scanner

# 或从本地路径安装
openclaw-cn plugins add ./skill-security-scanner
```

## 使用方法

### 命令行工具

安装后全局可用的 `skill-security-scan` 命令：

```bash
# 基本使用
skill-security-scan

# 指定输出格式
skill-security-scan --format markdown
skill-security-scan --format json
skill-security-scan --format text

# 指定扫描路径
skill-security-scan --scan-path /path/to/skills
skill-security-scan "C:\\path\\to\\skills"

# 查看帮助
skill-security-scan --help

# 查看版本
skill-security-scan --version
```

### 通过OpenClaw使用

```bash
# 运行安全扫描
openclaw-cn skill-security-scan --format markdown

# 指定扫描路径
openclaw-cn skill-security-scan --scan-path /path/to/skills --format json
```

## 配置

在OpenClaw配置文件中添加：

```yaml
plugins:
  entries:
    skill-security-scanner:
      config:
        scanPath: "/path/to/skills"
        sensitiveKeywords:
          - "exec"
          - "shell"
          - "rm"
          - "delete"
          - "format"
```

## 报告示例

### 风险统计
```
📊 风险统计:
  🔴 高风险: 2
  🟡 中风险: 48
  🟢 低风险: 2
```

### 木马检测摘要
```
🦠 木马检测摘要:
  检测技能: 52/52
  高风险: 0
  中风险: 0
  可疑文件: 0个
```

### 安全建议
```
💡 安全建议:
1. 立即审查高风险技能
2. 定期审查中风险技能
3. 提高文档覆盖率
4. 限制敏感操作的使用
5. 定期更新依赖
6. 实施代码审查流程
7. 使用沙盒环境
8. 建立技能白名单
9. 监控技能行为
10. 定期进行安全扫描
```

## 开发

### 构建

```bash
# 安装依赖
npm install

# 构建插件
npm run build

# 清理构建产物
npm run clean
```

## 许可证

MIT

## 支持

- GitHub Issues: https://github.com/openclaw/openclaw-cn/issues
- 文档: https://docs.openclaw.ai

## 版本历史

- **v1.0.2** (2026-03-09): 修复bug，优化性能
- **v1.0.1** (2026-03-09): 添加木马检测功能
- **v1.0.0** (2026-03-09): 初始版本发布

## 许可证

本技能使用MIT许可证发布。详情请参阅package.json中的许可证信息。