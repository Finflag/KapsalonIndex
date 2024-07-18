import sqlite3

# Verbinding maken met SQLite-database
conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()

# Aanmaken van de tabel 'dishes'
cursor.execute('''CREATE TABLE IF NOT EXISTS dishes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    price REAL,
                    city TEXT,
                    timestamp INTEGER
                )''')

# Aanmaken van de tabel 'average_prices'
cursor.execute('''CREATE TABLE IF NOT EXISTS average_prices (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city TEXT,
                    average_price REAL,
                    timestamp INTEGER
                )''')

# Commit en sluiten van de databaseverbinding
conn.commit()
conn.close()

print("SQLite database 'restaurants.db' is succesvol opgezet.")