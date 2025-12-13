import requests
from findMostStars import findMostStars
from storeRepoData import storeRepoData

# User inputs a GitHub username
username = input('Enter a GitHub username: ').strip()

# Error if username is empty
if not username:
    print('Error: Username cannot be empty')
    exit(1)

# Functions take it from here
try:
    sortedResults = findMostStars(username)
    storeRepoData(username, sortedResults)
# Centralized error handling
except ValueError as e: # Value error path (mapped from 404 error intentionally, because a 404 error is returned when a username is invalid)
    print(f'Error: {e}')
    exit(1)
except ConnectionError as e: # Network connection error path
    print(f'Error: {e}')
    exit(1)
except requests.exceptions.HTTPError as e: # HTTP error path not 404
    print(f'Error: {e}')
    exit(1)
except Exception as e: # Unexpected error path
    print(f'Unexpected error: {e}')
    exit(1)
    exit(1
