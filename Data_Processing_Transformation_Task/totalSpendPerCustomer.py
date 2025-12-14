import pandas as pd

def totalSpendPerCustomer(csv_file='../transactions.csv'): # Stores csv outside of the current directory
    df = pd.read_csv(csv_file) # Read the csv file and convert it into a pandas dataframe
    # Calculates the total spend per customer in the csv file and sorts the results in descending order via amount
    calculateTotalSpendPerCustomer = df.groupby('customer_id')['amount'].sum().sort_values(ascending=False).reset_index() # Using reset_index() so customer_id is a column, not an index, this is important for output formatting
    dfWithRenamedColumn = calculateTotalSpendPerCustomer.rename(columns={'amount': 'total_spend'}) # Rename the column 'amount' to 'total_spend'
    return dfWithRenamedColumn
