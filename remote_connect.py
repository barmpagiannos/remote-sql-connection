import pandas as pd
from sqlalchemy import create_engine
import sys

# --- LOGIN CREDENTIALS ---
USER = ''
PASSWORD = ''
HOST = '' # IPv4 address of Computer A (the one hosting the database).
DATABASE = '' # The name of the database from the SQL file.

def main():
    try:
        # LAN Connection String Creation.
        connection_url = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
        engine = create_engine(connection_url)

        # Query to retrieve Chefs from the student database.
        # We select first name, last name, and birth year.
        query = "SELECT first_name, last_name, birth_year FROM chefs ORDER BY last_name ASC;"

        # Convert to Pandas DataFrame.
        df = pd.read_sql(query, engine)

        if df.empty:
            print("Connection successful, but no data found in the 'chefs' table.")
        else:
            print("Connection successful! Data retrieved from Computer A:")
            print("-" * 50)
            print(df)
            print("-" * 50)
            print(f"Total number of Chefs: {len(df)}")

    except Exception as e:
        print(f"Error occurred while connecting: {e}")
        print("\nPlease check if:")
        print(f"1. Computer A ({HOST}) is powered on.")
        print("2. Both computers are on the same network.")
        print("3. The password is correct.")

if __name__ == "__main__":
    main()