import sqlite3

database = sqlite3.connect('intervention_app.db')

cursorObject = database.cursor()

cursorObject.execute('''CREATE TABLE IF NOT EXISTS intervention_app (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            description TEXT
                        )''')

print("SQLite database and table created successfully!")

database.commit()
database.close()