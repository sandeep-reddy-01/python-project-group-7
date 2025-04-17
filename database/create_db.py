import sqlite3
import pandas as pd

def save_to_db(df, db_name="database/elections.db", table_name="election_data"):
    """
    Saves the entire DataFrame into the specified SQLite database.
    
    Args:
        df (pd.DataFrame): DataFrame containing the election data.
        db_name (str): Path to the SQLite database file.
        table_name (str): Name of the table in the database to insert data into.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)
        
        # Insert the entire DataFrame into the specified table
        df.to_sql(table_name, conn, if_exists='replace', index=False)

        # Commit and close the connection
        conn.commit()
        conn.close()

        print(f"Data inserted successfully into table '{table_name}' in '{db_name}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

