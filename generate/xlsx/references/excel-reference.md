# Excel Reference

Detailed reference for Excel file operations, financial model standards, and formula verification.

## Financial Model Standards

### Color Coding Standards

Unless otherwise stated by the user or existing template:

- **Blue text (RGB: 0,0,255)**: Hardcoded inputs, scenario numbers
- **Black text (RGB: 0,0,0)**: ALL formulas and calculations
- **Green text (RGB: 0,128,0)**: Links from other worksheets in same workbook
- **Red text (RGB: 255,0,0)**: External links to other files
- **Yellow background (RGB: 255,255,0)**: Key assumptions needing attention

### Number Formatting Standards

- **Years**: Format as text strings ("2024" not "2,024")
- **Currency**: Use $#,##0 format; specify units in headers ("Revenue ($mm)")
- **Zeros**: Use formatting to make all zeros "-" (e.g., "$#,##0;($#,##0);-")
- **Percentages**: Default to 0.0% format (one decimal)
- **Multiples**: Format as 0.0x for valuation multiples
- **Negative numbers**: Use parentheses (123) not minus -123

### Formula Construction Rules

**Assumptions Placement**:
- Place ALL assumptions in separate assumption cells
- Use cell references instead of hardcoded values
- Example: `=B5*(1+$B$6)` instead of `=B5*1.05`

**Error Prevention**:
- Verify all cell references are correct
- Check for off-by-one errors in ranges
- Ensure consistent formulas across projection periods
- Test with edge cases (zero, negative)
- Verify no unintended circular references

**Documentation for Hardcodes**:
- Format: "Source: [System/Document], [Date], [Specific Reference], [URL if applicable]"
- Examples:
  - "Source: Company 10-K, FY2024, Page 45, Revenue Note, [SEC EDGAR URL]"
  - "Source: Bloomberg Terminal, 8/15/2025, AAPL US Equity"

## Formulas vs Hardcoded Values

**Always use Excel formulas instead of calculating in Python.**

### WRONG - Hardcoding
```python
total = df['Sales'].sum()
sheet['B10'] = total  # Hardcodes 5000
```

### CORRECT - Using Formulas
```python
sheet['B10'] = '=SUM(B2:B9)'
sheet['C5'] = '=(C4-C2)/C2'
sheet['D20'] = '=AVERAGE(D2:D19)'
```

## Creating New Excel Files

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()
sheet = wb.active
sheet['A1'] = 'Hello'
sheet.append(['Row', 'of', 'data'])
sheet['B2'] = '=SUM(A1:A10)'
sheet['A1'].font = Font(bold=True, color='FF0000')
sheet['A1'].fill = PatternFill('solid', start_color='FFFF00')
sheet['A1'].alignment = Alignment(horizontal='center')
sheet.column_dimensions['A'].width = 20
wb.save('output.xlsx')
```

## Editing Existing Excel Files

```python
from openpyxl import load_workbook

wb = load_workbook('existing.xlsx')
sheet = wb.active  # or wb['SheetName']
for sheet_name in wb.sheetnames:
    sheet = wb[sheet_name]

sheet['A1'] = 'New Value'
sheet.insert_rows(2)
sheet.delete_cols(3)
new_sheet = wb.create_sheet('NewSheet')
wb.save('modified.xlsx')
```

## Recalculating Formulas

```bash
python recalc.py <excel_file> [timeout_seconds]
```

The script:
- Automatically sets up LibreOffice macro on first run
- Recalculates all formulas in all sheets
- Scans ALL cells for Excel errors
- Returns JSON with detailed error locations
- Works on Linux and macOS

### Interpreting recalc.py Output
```json
{
  "status": "success",           // or "errors_found"
  "total_errors": 0,
  "total_formulas": 42,
  "error_summary": {
    "#REF!": {
      "count": 2,
      "locations": ["Sheet1!B5", "Sheet1!C10"]
    }
  }
}
```

## Formula Verification Checklist

### Essential Verification
- Test 2-3 sample references before building full model
- Confirm Excel columns match (column 64 = BL, not BK)
- Remember Excel rows are 1-indexed (DataFrame row 5 = Excel row 6)

### Common Pitfalls
- NaN handling: Check with `pd.notna()`
- Far-right columns: FY data often in columns 50+
- Multiple matches: Search all occurrences, not just first
- Division by zero: Check denominators (#DIV/0!)
- Wrong references: Verify all cell references (#REF!)
- Cross-sheet references: Use correct format (Sheet1!A1)

### Formula Testing Strategy
- Start small: Test on 2-3 cells before applying broadly
- Verify dependencies: Check all referenced cells exist
- Test edge cases: Zero, negative, very large values

## Best Practices

### Library Selection
- **pandas**: Data analysis, bulk operations, simple export
- **openpyxl**: Complex formatting, formulas, Excel-specific features

### Working with openpyxl
- Cell indices are 1-based
- `data_only=True` reads calculated values
- **Warning**: If opened with `data_only=True` and saved, formulas are permanently lost
- Large files: Use `read_only=True` or `write_only=True`

### Working with pandas
- Specify data types: `pd.read_excel('file.xlsx', dtype={'id': str})`
- Read specific columns: `pd.read_excel('file.xlsx', usecols=['A', 'C', 'E'])`
- Handle dates: `pd.read_excel('file.xlsx', parse_dates=['date_column'])`
