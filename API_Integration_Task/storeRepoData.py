import sqlite3

def storeRepoData(username, sortedResults):
    # Using context manager ensures connection is closed even if an error occurs
    with sqlite3.connect('../repos.db') as conn: # Creates db file if it doesn't exist, if it does, it connects to it
        cursor = conn.cursor() # Allows us to execute SQL commands
        
        # Create the repos table if it doesn't exist.
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS repos (
                repoName TEXT,
                lastUpdatedDate TEXT,
                starsCount INTEGER
            )
        ''')
        # Delete all rows from the repos table so each run is fresh
        cursor.execute('DELETE FROM repos')
        
        # Goes into the sortedResults list and inserts the repoName, lastUpdatedDate, and starsCount into the repos table
        for repoName, data in sortedResults:
            cursor.execute('''
                INSERT INTO repos (repoName, lastUpdatedDate, starsCount)
                VALUES (?, ?, ?)
            ''', (repoName, data['lastUpdatedDate'], data['starsCount']))
        
        # Commits the changes to the database (connection closes automatically after this block)
        conn.commit()
    
    print(f'Successfully stored {len(sortedResults)} repos in repos.db\n')
    
    print('Stored repos:')
    for repoName, data in sortedResults:
        print(f"  {repoName}, last updated: {data['lastUpdatedDate']}, stars: {data['starsCount']}")
    

    if sortedResults:
        mostStarredRepo = sortedResults[0] # 0th index is the most starred repo because we sorted earlier.
        print(f"\nMost starred repo: {mostStarredRepo[0]} with {mostStarredRepo[1]['starsCount']} stars.")

