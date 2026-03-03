---
name: xlsx
description: "Comprehensive spreadsheet creation, editing, and analysis with support for formulas, formatting, data analysis, and visualization. When Claude needs to work with spreadsheets (.xlsx, .xlsm, .csv, .tsv, etc) for: (1) Creating new spreadsheets with formulas and formatting, (2) Reading or analyzing data, (3) Modify existing spreadsheets while preserving formulas, (4) Data analysis and visualization in spreadsheets, or (5) Recalculating formulas. Do not use for: Google Sheets, Word documents (use docx skill), database operations, or pure data analysis without spreadsheet output (use pandas directly)."
license: Proprietary. LICENSE.txt has complete terms
---

# Requirements for Outputs

## All Excel files

### Zero Formula Errors
Every Excel model MUST be delivered with ZERO formula errors (#REF!, #DIV/0!, #VALUE!, #N/A, #NAME?)

### Preserve Existing Templates
Study and EXACTLY match existing format, style, and conventions when modifying files.

## XLSX creation, editing, and analysis

### Important Requirements

**LibreOffice Required for Formula Recalculation**: Use the `recalc.py` script. Automatically configures on first run.

### Reading and analyzing data

```python
import pandas as pd
df = pd.read_excel('file.xlsx')                    # Default: first sheet
all_sheets = pd.read_excel('file.xlsx', sheet_name=None)  # All sheets
df.head(); df.info(); df.describe()                # Analyze
```

## CRITICAL: Use Formulas, Not Hardcoded Values

Always use Excel formulas instead of calculating in Python. The spreadsheet must remain dynamic.

```python
# WRONG: sheet['B10'] = df['Sales'].sum()
# CORRECT:
sheet['B10'] = '=SUM(B2:B9)'
sheet['C5'] = '=(C4-C2)/C2'
```

## Common Workflow

1. **Choose tool**: pandas for data, openpyxl for formulas/formatting
2. **Create/Load**: New workbook or existing file
3. **Modify**: Add/edit data, formulas, formatting
4. **Save**: Write to file
5. **Recalculate (MANDATORY IF USING FORMULAS)**: `python recalc.py output.xlsx`
6. **Verify**: Fix any errors from recalc output, recalculate again

## Recalculating Formulas

```bash
python recalc.py <excel_file> [timeout_seconds]
```

Returns JSON with status, error count, formula count, and error locations.

## Code Style Guidelines

Write minimal, concise Python code. Avoid verbose variable names, redundant operations, and unnecessary print statements.

## Detailed Reference

For financial model standards (color coding, number formatting, formula construction rules), openpyxl/pandas examples, formula verification checklist, and best practices, see [references/excel-reference.md](references/excel-reference.md).
