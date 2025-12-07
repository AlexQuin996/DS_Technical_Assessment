from getRepoData import getRepoData

# Finds the most starred repository for a given GitHub username
def findMostStars(username):
    # Gets the repository data from the GitHub API
    jsonResponse = getRepoData(username)
    resultsDict = {}
    jsonResponseLength = len(jsonResponse)

    # For the length of the given repo, we loop thru each repo response and get the repository name, last updated date, and stars count
    for i in range(jsonResponseLength):
        repoName = jsonResponse[i]['name']
        lastUpdatedDate = jsonResponse[i]['updated_at']
        starsCount = jsonResponse[i]['stargazers_count']
        
        # Adds the repository name, last updated date, and stars count to the results dictionary
        resultsDict[repoName] = {
            'lastUpdatedDate': lastUpdatedDate,
            'starsCount': starsCount
        }
    
    # Sorts the results dictionary by stars count in descending order
    sortedResults = sorted(resultsDict.items(), key=lambda x: x[1]['starsCount'], reverse=True)
    return sortedResults
