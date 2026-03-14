---
name: finance-accounting
description: Comprehensive financial accounting document processing skill package - includes bookkeeping, reconciliation, tax, reporting and other core functions.
tags: [accounting, finance, tax, document, invoice]
version: "1.0.0"
---

# Finance Accounting Skill

## Overview
This skill package provides complete financial accounting document processing functions, including bookkeeping, reconciliation, tax calculation, report generation and other core business processes.

## Function Modules

### 1. Basic Bookkeeping Module
- **Transaction Recording**: Income, expense, transfer records
- **Account Management**: Chart of accounts setup and classification
- **Voucher Generation**: Automatic accounting voucher generation
- **Balance Calculation**: Real-time account balance calculation

### 2. Reconciliation Module
- **Bank Reconciliation**: Automatic bank statement matching
- **Counterparty Reconciliation**: Customer/supplier reconciliation
- **Difference Handling**: Automatic difference identification and processing
- **Reconciliation Report**: Generate reconciliation reports

### 3. Tax Module
- **VAT Calculation**: Automatic VAT calculation
- **Income Tax Prepayment**: Personal income tax/Corporate income tax
- **Tax Declaration**: Generate tax declaration forms
- **Tax Planning**: Tax optimization suggestions

### 4. Report Module
- **Balance Sheet**: Automatic balance sheet generation
- **Income Statement**: Generate income statement
- **Cash Flow Statement**: Cash flow analysis
- **Custom Reports**: On-demand report generation

### 5. Document Generation
- **Invoice Generation**: Automatic electronic invoice generation
- **Reconciliation Statement**: Customer reconciliation statements
- **Tax Report**: Tax declaration documents
- **Audit Report**: Audit required documents

## Usage

### Basic Bookkeeping
```bash
# Record income
python finance.py record --type income --amount 1000 --category "Sales Revenue" --date "2026-02-28"

# Record expense
python finance.py record --type expense --amount 500 --category "Office Supplies" --date "2026-02-28"

# View balance
python finance.py balance
```

### Reconciliation Processing
```bash
# Import bank statements
python finance.py reconcile import --file bank_statement.csv

# Auto reconciliation
python finance.py reconcile auto

# Generate reconciliation report
python finance.py reconcile report --output reconciliation_report.pdf
```

### Tax Calculation
```bash
# Calculate VAT
python finance.py tax vat --period 2026-02

# Generate tax declaration report
python finance.py tax report --type vat --period 2026-02 --output vat_report.xlsx

# Tax planning suggestions
python finance.py tax plan --year 2026
```

### Report Generation
```bash
# Generate balance sheet
python finance.py report balance-sheet --period 2026-02 --output balance_sheet.pdf

# Generate income statement
python finance.py report income-statement --period 2026-02 --output income_statement.pdf

# Generate cash flow statement
python finance.py report cash-flow --period 2026-02 --output cash_flow.pdf
```

## Configuration Files

### Chart of Accounts Setup
```yaml
# config/accounts.yaml
accounts:
  assets:
    - code: 1001
      name: Cash
      type: current_asset
    - code: 1002
      name: Bank Deposits
      type: current_asset

  liabilities:
    - code: 2001
      name: Short-term Loans
      type: current_liability

  equity:
    - code: 3001
      name: Paid-in Capital
      type: equity

  income:
    - code: 4001
      name: Main Business Revenue
      type: revenue

  expenses:
    - code: 5001
      name: Office Expenses
      type: expense
```

### Tax Setup
```yaml
# config/tax.yaml
tax:
  vat_rate: 0.13  # VAT rate
  income_tax_rate: 0.25  # Corporate income tax rate
  tax_threshold: 300000  # Tax threshold

  declarations:
    vat: monthly  # VAT declaration cycle
    income_tax: quarterly  # Income tax declaration cycle
```

## Data Format

### Transaction Record Format
```csv
date,type,account,amount,description,category
2026-02-28,income,4001,1000.00,Product sales,Sales revenue
2026-02-28,expense,5001,500.00,Office supplies purchase,Office expenses
```

### Bank Statement Format
```csv
date,description,amount,balance
2026-02-28,Salary income,10000.00,15000.00
2026-02-28,Utilities expense,-500.00,14500.00
```

## Integration Features

### Integration with Existing Skills
- **github skill**: Version control financial data
- **tavily-search skill**: Search tax regulations
- **proactive-agent skill**: Automatically execute periodic tasks

### External System Integration
- **Bank API**: Automatic bank statement retrieval
- **Tax System**: Electronic declaration interface
- **ERP System**: Enterprise resource planning integration

## Security Considerations

### Data Security
- Financial data encrypted storage
- Access permission control
- Operation log recording

### Compliance
- Compliance with accounting standards
- Compliance with tax regulations
- Audit trail

## Troubleshooting

### Common Issues
1. **Data import failure**: Check file format and encoding
2. **Calculation errors**: Verify chart of accounts setup
3. **Report generation failure**: Check dependency library installation

### Log Viewing
```bash
# View run logs
tail -f logs/finance.log

# View error logs
tail -f logs/error.log
```

## Update Plan

### Recent Updates
- [ ] Add more report templates
- [ ] Support more bank formats
- [ ] Optimize tax calculation algorithm

### Long-term Planning
- [ ] AI intelligent analysis features
- [ ] Forecast and budget features
- [ ] Multi-language support

---

**Skill Status**: ✅ Ready
**Last Updated**: 2026-02-28
**Maintainer**: Tianyuan (⚡)
