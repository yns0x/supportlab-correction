import sqlite3

conn = sqlite3.connect('supportlab.db')
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titre TEXT NOT NULL,
        description TEXT NOT NULL,
        categorie TEXT NOT NULL,
        priorite TEXT NOT NULL,
        statut TEXT NOT NULL,
        note TEXT,
        date_creation TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
)

conn.commit()
conn.close()

print("Base de données initialisée.")