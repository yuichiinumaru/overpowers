---
name: ai-employee-collab
description: "AI employee collaboration skills package - MultiAI role configuration, task automation, progress monitoring, result reporting. Suitable for teams wanting automated operations."
metadata:
  openclaw:
    category: "ai"
    tags: ['ai', 'automation', 'generation']
    version: "1.0.0"
---

# AI Employee Collaboration Skills Package

## One-Sentence Introduction
Organizes multiple AI roles into virtual teams, automatically assigning tasks, monitoring progress, and reporting results.

## What Problems Is It Solved?
- One person cannot manage: multiple projects in parallel → AI team automatically divides tasks
- Task distribution is uneven: unaware of who should do what → Intelligent task allocation
- Progress tracking is difficult: constantly asking about progress → Automated status reporting
- Collaboration efficiency is low: high communication costs → Structured workflow

## Core Features
- 🤖 Multi-AI role configuration: Manager, Product, Technology, Testing, Operations...
- 📋 Intelligent task assignment: Automatically assign tasks based on roles
- 📊 Real-time status monitoring: View each employee's work status
- 📝 Automated result reporting: Daily, weekly reports, task completion notifications
- 🔄 Workflow scheduling: Define task flow rules
- 💾 Long-term memory retention: AI employees retain long-term knowledge

## Quick Start

### Installation
```bash
cd ai-employee-skill
npm install
```

### Configure Employees
Edit `config/employees.json`:
```json
{
  "employees": [
    {
      "id": "boss",
      "name": "Strategic Decision Maker",
      "role": "Strategic Decision Making",
      "skills": ["Strategic Analysis", "Resource Allocation", "Performance Evaluation"]
    },
    {
      "id": "pm",
      "name": "Product Planning",
      "role": "Product Planning",
      "skills": ["Requirement Analysis", "Product Design", "Document Writing"]
    }
  ]
}
```

### Launch Company
```bash
npm start
```

## Command List

| Command | Explanation |
|---------|-------------|
| `/hire <role>` | Recruit AI employees |
| `/fire <id>` | Terminate AI employees |
| `/assign <task>` | Assign tasks |
| `/status` | Check team status |
| `/report [report type]` | Generate work reports |
| `/meeting` | Hold team meetings |

## File Structure  
```
ai-employee-skill/  
├── SKILL.md              # Skills Explanation  
├── README.md             # Product Documentation  
├── TUTORIAL.md           # Usage Guide  
├── package.json          # Dependency Configuration  
├── config.json           # System Configuration  
├── scripts/              # Core Scripts  
│   ├── employee-manager.js   # Employee Management  
│   ├── task-dispatcher.js    # Task Distribution  
│   ├── status-monitor.js     # Status Monitoring  
│   ├── report-generator.js   # Report Generation  
│   └── meeting-coordinator.js # Meeting Coordination  
├── templates/            # Employee Templates  
│   ├── boss-ai.md  
│   ├── product-ai.md  
│   ├── tech-ai.md  
│   ├── test-ai.md  
│   └── operation-ai.md  
└── examples/             # Example Scenarios  
    ├── startup-team.json  
    └── content-team.json  
```

## Employee Role Descriptions  

| Role          | Responsibilities | Core Capabilities |  
|---------------|------------------|-------------------|  
| Board AI      | Strategic Decision-Making | Market Analysis, Resource Allocation, Performance Evaluation |  
| Product AI     | Product Planning      | Demand Analysis, Product Design, PRD Writing |  
| Technical AI   | Technical Development | Architecture Design, Coding Implementation, Code Review |  
| Testing AI     | Quality Assurance     | Testing Plans, Automation Testing, Bug Tracking |  
| Operations AI  | Growth Operations      | Content Creation, User Operations, Data Analysis |  
| Financial AI   | Financial Management   | Cost Calculation, ROI Analysis, Budget Planning |  
| HR-AI         | Human Resources      | Recruitment Management, Performance Evaluation, Training Development |  

All markdown preserved, no additional text.

┌─────────────────────────────────────────────────────────────┐  
│    任务流程              │  
├─────────────────────────────────────────────────────────────┤  
│    产品AI  │ →  产品AI  │ →  技术AI  │ →  测试AI  │  
├─────────────────────────────────────────────────────────────┤  
│ 下达   │ 需求    │ 开发    │ 验收    │  
└─────────────────────────────────────────────────────────────┘  
```

## 适用人群  
- 独立开发者：一人即团队  
- 小型创业团队：人手不够AI来凑  
- 自媒体运营：内容批量生产  
- 项目管理者：多项目并行管理  
- 自动化爱好者：AI协作实践  

## 定价  
- 基础版：¥199（5个员工角色 + 基础工作流）  
- 专业版：¥399（无限角色 + 自定义工作流 + API接口）  
- 企业版：¥999（私有部署 + 定制开发 + 技术支持）  

---  

*开发者：AI-Company*  
*联系：通过ClawHub*
