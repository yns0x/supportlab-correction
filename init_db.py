import sqlite3

conn = sqlite3.connect('supportlab.db')
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        description TEXT NOT NULL,
        priorite TEXT NOT NULL,
        statut TEXT NOT NULL
    );
    """
)

conn.commit()
conn.close()

print("Base de données initialisée.")