#!/usr/bin/env python3
import sys
import argparse

def generate_schema_doc(table_name):
    template = f"""## Table: {table_name}

**Description**: [What this table represents]
**Grain**: [One row per...]
**Primary Key**: [column(s)]
**Row Count**: [approximate, with date]
**Update Frequency**: [real-time / hourly / daily / weekly]
**Owner**: [team or person responsible]

### Key Columns

| Column | Type | Description | Example Values | Notes |
|--------|------|-------------|----------------|-------|
| id | STRING | Primary identifier | "row_123" | PK |
| [col_name] | [TYPE] | [description] | [example] | [notes] |

### Relationships
- Joins to `[parent_table]` on `[fk_column]`
- Parent of `[child_table]` (1:many on `[pk_column]`)

### Known Issues
- [List any known data quality issues]
- [Note any gotchas for analysts]

### Common Query Patterns
- [Typical use cases for this table]
"""
    return template

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Schema Documentation template.")
    parser.add_argument("--table", required=True, help="Table name")
    parser.add_argument("--out", default="schema-doc.md", help="Output file name")
    args = parser.parse_args()

    with open(args.out, 'w') as f:
        f.write(generate_schema_doc(args.table))

    print(f"Generated schema documentation template for '{args.table}' at {args.out}")
