import requests

# Gets the repository data from the GitHub API
def getRepoData(username):
    # Creates the URL for the GitHub API
    reposUrl = f'https://api.github.com/users/{username}/repos'
    try:
        response = requests.get(reposUrl, timeout=10) # Gets the response from the GitHub API, times out after 10 seconds
        response.raise_for_status() # If any HTTP error gets caught here, it will skip down to the except blocks
        return response.json() # Returns the response from the GitHub API
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404: # If the user is not found on GitHub, error w/404
            raise ValueError(f'User "{username}" not found on GitHub')
        else: # If the GitHub API returns an HTTP error other than 404, error w/status code
            raise requests.exceptions.HTTPError(f'GitHub API returned status code {response.status_code}')
    except requests.exceptions.RequestException as e: # Network failure path
        raise ConnectionError(f'Failed to connect to GitHub API - {e}')