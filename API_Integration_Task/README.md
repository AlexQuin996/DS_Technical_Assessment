# GitHub Repo Analyzer

This script fetches repository data from the GitHub API for a given username, counts how mant people have 'starred' the repo, its most recent update date, and stores said data in a SQLite database called repos.db.

## Setup

Make sure you have Python installed. The only library you need to install is `requests`:

```bash
pip install requests
```

Note: `sqlite3` comes built-in with Python, so no installation needed.

## Running the Script

1. Run the main script:

```bash
python main.py
```

2. When prompted, enter a GitHub username (e.g., `torvalds` or `octocat`)

The script:
- Fetches all repositories for that user from the GitHub Public API
- Grabs latest update date
- Sorts them by star count (descending)
- Stores them in `repos.db`
- Prints out all repos with their last updated date and star count
- Shows which repo has the most stars

## What It Does

- `getRepoData.py` - Handles the GitHub API call and error handling
- `findMostStars.py` - Processes the API response and sorts repos by stars
- `storeRepoData.py` - Stores the results in a SQLite database and prints them out
- `main.py` - Entry point that ties everything together

## Notes

- The database file (`repos.db`) gets cleared and repopulated each time you run the script, and is stored one layer above this folder (`DS_Technical_Assessment/repos.db`)
- If the username doesn't exist or there's a network error, the script will exit with an error message
- The script uses a 10 second timeout for API requests
