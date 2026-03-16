---
name: food-expiry-reminder
description: "Food expiry reminder skill. Used to record, manage, and remind about food expiry. Use this skill when users need to record food information, check if food has expired, view upcoming expiring food, or manage food inventory. Data is stored in the food_data.json file."
metadata:
  openclaw:
    category: "productivity"
    tags: ['productivity', 'reminder', 'alert']
    version: "1.0.0"
---

# Food Expiry Reminder Skill

This skill helps users record, manage, and receive reminders about food expiry. All food data is stored in the `food_data.json` file.

## Feature Overview

1. **Record Food Information** - Add new food entries.
2. **Check Expiry Status** - Check if food is expired or nearing expiry.
3. **View All Foods** - List all foods and their statuses.
4. **Reminder Function** - Remind about food expiring within a week.
5. **Data Management** - Update or delete food entries.

## Data Structure

Food data is stored in the `food_data.json` file with the following format:

```json
{
  "foods": [
    {
      "id": "unique identifier",
      "name": "food name",
      "production_date": "production date (YYYY-MM-DD)",
      "expiry_days": "shelf life in days",
      "expiry_date": "expiry date (automatically calculated)",
      "location": "storage location",
      "quantity": "quantity",
      "notes": "remarks",
      "created_at": "creation timestamp",
      "updated_at": "update timestamp"
    }
  ]
}
```

## Usage

### 1. Add New Food

Use the following command to add a new food entry:

```bash
python scripts/add_food.py "Food Name" "Production Date" "Shelf Life in Days" "Storage Location" "Quantity" "Notes"
```

Alternatively, you can manually edit the `food_data.json` file.

### 2. Check Expiry Status

Run the check script to view expired and soon-to-expire foods:

```bash
python scripts/check_expiry.py
```

### 3. View All Foods

View all currently stored foods:

```bash
python scripts/list_foods.py
```

### 4. Get Reminders

Get reminders for foods expiring within a week:

```bash
python scripts/get_reminders.py
```

## Script Descriptions

### `scripts/add_food.py`

Adds a new food item to the database. Arguments:
- Food name
- Production date (YYYY-MM-DD)
- Shelf life in days (integer)
- Storage location
- Quantity (optional, defaults to 1)
- Notes (optional)

### `scripts/check_expiry.py`

Checks the expiry status of all foods and displays:
- Expired foods
- Foods expiring within a week
- Foods expiring within two weeks
- Safe foods

### `scripts/list_foods.py`

Lists detailed information for all foods, including their status.

### `scripts/get_reminders.py`

Specifically retrieves reminders for foods expiring within a week.

### `scripts/init_data.py`

Initializes the `food_data.json` file (if it doesn't exist).

## Workflow

1. **Initialize Data File** - Run `init_data.py` on first use.
2. **Add Food Records** - Record new food items immediately after purchase.
3. **Regular Checks** - Run `check_expiry.py` daily or weekly.
4. **Handle Reminders** - Address soon-to-expire foods based on reminders.

## Notes

1. The production date format must be YYYY-MM-DD.
2. Shelf life in days must be an integer.
3. The expiry date is automatically calculated.
4. It is recommended to run the check script once daily.
5. The data file is located at `data/food_data.json`.

## References

- [Data Structure Explanation](references/data_structure.md)
- [Usage Examples](references/examples.md)
- [Frequently Asked Questions](references/faq.md)
