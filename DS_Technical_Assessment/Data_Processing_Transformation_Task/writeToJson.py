import json

def writeToJson(finalResults, filename='top_customers.json'):
    # Creates JSON file, loops through the dictionary list and writes the data to the file
    with open(filename, 'w') as jsonFile:
        jsonFile.write('[\n') # Formatting
        for i, record in enumerate(finalResults): # Loops through the dictionary list via enumerate to map the index
            jsonFile.write('  ' + json.dumps(record, separators=(', ', ':'))) # Formats the data to be written to the file
            if i < len(finalResults) - 1: # We only want to add a comma if it's not the last item
                jsonFile.write(',') # Formatting
            jsonFile.write('\n') # Formatting
        jsonFile.write(']') # Formatting

