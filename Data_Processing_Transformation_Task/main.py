from totalSpendPerCustomer import totalSpendPerCustomer
from top5CustomersByTotalSpend import top5CustomersByTotalSpend
from writeToJson import writeToJson

# Calculates spending for all customers in the csv file that is passed here, or will use csv file defined in totalSpendPerCustomer.py if nothing is passed here
totalSpendingPerCustomer = totalSpendPerCustomer()

# Gets the top 5 customers by total spend
top5Customers = top5CustomersByTotalSpend(totalSpendingPerCustomer)

# Converts the dataframe to a list of dictionaries to be written to the JSON file
finalResults = top5Customers.to_dict(orient='records')

# Writes the list of dictionaries to a JSON file
writeToJson(finalResults)
