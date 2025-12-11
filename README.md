# Excel Automation Tool

This is a small Python script that automates the processing of Excel files.

## What it does

- Loads an Excel file (`input.xlsx`)
- Removes rows that are completely empty
- Adds a new column called `Total` that contains the sum of all numeric values in each row
- Saves the cleaned data to `output.xlsx`

## Requirements

- Python 3
- pandas
- openpyxl

Install dependencies with:

```bash
pip3 install -r requirements.txt
