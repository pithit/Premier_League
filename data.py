import pandas as pd
import sqlite3

# URL of the CSV file containing soccer data
url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-04-04/soccer21-22.csv'

try:
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(url)

    # Connect to the SQLite database
    with sqlite3.connect("flights.db") as conn:
        # Create a table directly from the DataFrame
        df.to_sql("soccer", conn, if_exists="replace", index=False)

        # SQL query to select the first 5 rows from the "soccer" table
        query = "SELECT * FROM soccer ;"  # LIMIT 5

        # Execute the query and load the results into a DataFrame
        result_df = pd.read_sql_query(query, conn)

    # Connection automatically closed when exiting the 'with' block

except Exception as e:
    # Print an error message if an exception occurs
    print(f"Error reading the CSV file: {e}")
