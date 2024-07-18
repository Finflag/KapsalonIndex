import sqlite3
import pandas as pd

# Functie om gegevens uit de database te halen en te sorteren
def fetch_and_sort_data():
    # Verbinding maken met de SQLite-database
    conn = sqlite3.connect('restaurants.db')

    # Query om gegevens op te halen en te sorteren op plaatsnaam en timestamp
    query = '''
        SELECT city, timestamp, AVG(price) AS average_price
        FROM dishes
        GROUP BY timestamp, city
        ORDER BY timestamp ASC, city ASC
    '''

    # Gegevens ophalen met behulp van Pandas DataFrame
    df = pd.read_sql_query(query, conn)

    # Databaseverbinding sluiten
    conn.close()

    return df

# Uitvoeren van de functie om gegevens op te halen en te sorteren
sorted_data = fetch_and_sort_data()

# Resultaten weergeven
print("Gemiddelde prijs per tijdstip per plaatsnaam:")
print(sorted_data)