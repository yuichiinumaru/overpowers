---
name: zhichu-tracker
description: ">"
metadata:
  openclaw:
    category: "tracking"
    tags: ['tracking', 'monitoring', 'analytics']
    version: "1.0.0"
---

# Smart Expense Tracker

An intelligent tool for quick bookkeeping through natural language and automatic generation of financial reports.

## Features

- 📝 **Natural Language Bookkeeping**: "Spent 35 yuan on lunch today", "Received salary of 8000"
- 🏷️ **Smart Automatic Categorization**: Automatically identifies categories like dining, transportation, shopping, etc.
- 📊 **Multi-dimensional Reports**: Daily, weekly, monthly reports, trend analysis
- 🔒 **Local Data Storage**: JSON file storage for privacy protection
- 🌐 **Chinese and English Support**: Supports Chinese and English natural language input
- ⚠️ **Abnormal Spending Detection**: Automatically identifies unusual spending patterns

## Quick Start

### Adding Expense and Income Records

```bash
# Record expenses
python scripts/expense-tracker.py add "今天午饭花了35元"
python scripts/expense-tracker.py add "昨天打车去公司28块"
python scripts/expense-tracker.py add "买衣服花了299元"

# Record income
python scripts/expense-tracker.py add "今天发工资8000元"
python scripts/expense-tracker.py add "收到红包200"
```

### Viewing Records

```bash
# List records from the last 7 days
python scripts/expense-tracker.py list

# List records from the last 30 days
python scripts/expense-tracker.py list 30

# Show only expenses
python scripts/expense-tracker.py list 7 expense
```

### Generating Reports

```bash
# Daily report
python scripts/report-generator.py daily
python scripts/report-generator.py daily 2024-01-15

# Weekly report
python scripts/report-generator.py weekly
python scripts/report-generator.py weekly 1  # Last week

# Monthly report
python scripts/report-generator.py monthly
python scripts/report-generator.py monthly 1  # Last month

# Trend analysis
python scripts/report-generator.py trend 30
```

### Viewing Statistics

```bash
# Expense and income summary for the last 30 days
python scripts/expense-tracker.py summary

# Summary for the last 90 days
python scripts/expense-tracker.py summary 90

# View category list
python scripts/expense-tracker.py categories
```

## Project Structure

```
smart-expense-tracker/
├── SKILL.md                      # This file
├── scripts/
│   ├── expense-tracker.py       # Core bookkeeping logic
│   └── report-generator.py      # Report generator
└── assets/
    └── categories.json          # Category configuration
```

## Data Storage

- **Path**: `~/.openclaw/workspace/data/expenses/expenses.json`
- **Format**: JSON
- **Privacy**: Purely local storage, no cloud upload

Data structure:
```json
{
  "expenses": [
    {
      "id": "a1b2c3d4",
      "date": "2024-01-15",
      "type": "expense",
      "amount": 35.00,
      "category": "餐饮",
      "note": "午饭",
      "raw_text": "今天午饭花了35元",
      "created_at": "2024-01-15T12:30:00"
    }
  ],
  "categories": {
    "income": ["工资", "奖金", "投资", ...],
    "expense": ["餐饮", "交通", "购物", ...]
  }
}
```

## Natural Language Support Examples

### Time Expressions
- "今天..." - Today
- "昨天..." - Yesterday
- "前天..." - The day before yesterday
- "2024-01-15..." - Specific date

### Amount Expressions
- "花了35元"
- "花了35块"
- "35元"
- "收入5000"

### Automatic Categorization Keywords

| Category | Trigger Keywords |
|------|-----------|
| Dining | 吃饭、午饭、晚饭、外卖、奶茶、咖啡、火锅 |
| Transportation | 地铁、公交、打车、滴滴、加油、停车、高铁 |
| Shopping | 购物、买衣服、鞋子、包包、化妆品、淘宝、京东 |
| Entertainment | 电影、游戏、充值、会员、旅游、KTV |
| Housing | 房租、房贷、水电、物业费、装修 |
| Salary | 工资、薪水、发工资 |
| Bonus | 奖金、年终奖、分红 |

## Category Configuration

Category configurations are stored in `assets/categories.json`, including:

- **Income Categories**: Salary, Bonus, Investment, Part-time, Red Packet, Refund, Other Income
- **Expense Categories**: Dining, Transportation, Shopping, Entertainment, Housing, Medical, Education, Communication, Social, Other Expenses
- **Budget Alerts**: Set budget thresholds for each category
- **Keyword Mapping**: Customize keywords for category recognition

### Custom Categories

Edit `assets/categories.json` to add custom categories and keywords.

## Report Types

### Daily Report
- Daily income and expense overview
- Category details
- Transaction record list

### Weekly Report
- Weekly income and expense overview
- Average daily spending
- Daily details
- TOP spending categories

### Monthly Report
- Monthly income and expense overview
- Budget execution status
- Weekly trends
- Category statistics
- Average daily spending

### Trend Analysis
- Spending trends (upward/downward/stable)
- Abnormal spending detection (exceeding 2 times the average)
- Month-on-month change analysis
- Spending recommendations

## Advanced Usage

### Deleting Records

```bash
# Delete record with specified ID
python scripts/expense-tracker.py delete a1b2c3d4
```

### JSON Output

```bash
# Report output in JSON format (for programmatic processing)
python scripts/report-generator.py monthly 0 json
```

### Batch Import

Batch import can be achieved by directly editing the `expenses.json` file.

## Usage Recommendations

1. **Daily Bookkeeping**: Develop a habit of recording daily expenses, spending 2 minutes each evening to review the day's spending.
2. **Timely Categorization**: If automatic categorization is inaccurate, add more specific keywords in the notes.
3. **Regular Review**: Check weekly reports every week and monthly reports every month to understand your spending patterns.
4. **Set Budgets**: Set budget alert values for each category in `categories.json`.

## Troubleshooting

### Amount Not Recognized
- Ensure the amount format is correct, e.g., "35元", "35块".
- Try to be more explicit: "花了35元".

### Inaccurate Categorization
- Add more keywords in the description, e.g., "淘宝买衣服" is more accurate than "买衣服".
- You can add custom keywords in `categories.json`.

### Corrupted Data File
- The data file is pure JSON and can be repaired with a text editor.
- It is recommended to back up `~/.openclaw/workspace/data/expenses/expenses.json` regularly.

## Extension Development

### Adding New Automatic Categorization Rules

Edit the `KEYWORD_MAPPING` dictionary in `scripts/expense-tracker.py`:

```python
KEYWORD_MAPPING = {
    # Existing rules...
    "新关键词": "目标分类",
    " another keyword": "Category Name"
}
```

### Integrating with Other Tools

`expense-tracker.py` can be imported as a module:

```python
from scripts.expense_tracker import ExpenseTracker

tracker = ExpenseTracker()
record = tracker.add("今天买书花了50元")
print(record)
```

## Technical Specifications

- **Python Version**: 3.9+
- **Dependencies**: No external dependencies, only standard libraries used
- **Encoding**: UTF-8
- **Data Format**: JSON

## License

MIT License
