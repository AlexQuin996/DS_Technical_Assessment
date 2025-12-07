# Data Processing & Transformation Task

This script processes transaction data from a .csv file to find the total spending per customer as well top 5 customers by total spending and outputs the results to a JSON file.

## Setup

Make sure you have Python installed. The script uses `pandas` (which you may need to install) and `json` (which comes built-in with Python, so no installation needed).

If you get an import error for pandas, install it with:

```bash
pip install pandas
```

## Running the Script

1. Place your `transactions.csv` file one directory up from this folder (the script looks for `../transactions.csv`), or where ever you feel like really. I store it outside this folder for seperation of concern reasons, but you could hypotheically put it anywhere, just make sure you know the file address.

2. Run the main script:

```bash
python main.py
```

The script:
- Reads the transactions CSV file
- Calculates total spending per customer
- Identifies the top 5 customers by total spend
- Writes the results to `top_customers.json` in the current directory

## Output

The results are saved to `top_customers.json` with the following format:

```json
[
  {"customer_id": 123, "total_spend": 5000.00},
  {"customer_id": 456, "total_spend": 4500.00},
  ...
]
```

## File Structure

- `main.py` - Main entry point that orchestrates the data processing
- `totalSpendPerCustomer.py` - Calculates total spending per customer from the CSV
- `top5CustomersByTotalSpend.py` - Filters to the top 5 customers
- `writeToJson.py` - Writes the results to a formatted JSON file
- `top_customers.json` - Formatted JSON file with final results after script runs
