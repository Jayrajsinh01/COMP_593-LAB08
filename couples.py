import sqlite3
import pandas as pd

con = sqlite3.connect('social_network.db')
mycursor = con.cursor()

# Query used to get all maaried couples
couples_query = """
SELECT person1.name AS person1_name, person2.name AS person2_name, start_date, type

FROM relationships
JOIN people person1 ON person1_id = person1.id
JOIN people person2 ON person2_id = person2.id
WHERE type = 'spouse';
"""

# Execute the query and fetch entire output
mycursor.execute(couples_query)
couples = mycursor.fetchall()

# Converting the output to a pandas DataFrame object
couples_df = pd.DataFrame(couples, columns=['COUPLE1', 'COUPLE2', 'start_date'])

# Generating a CSV file containing all married couples related information
couples_df.to_csv('couples.csv', index=False)

con.close()