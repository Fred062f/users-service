import sqlite3

def init_db():
    """Initializes the database and populates it with sample data."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)
    
    sample_data = [
        ("user_1", "1234"),
        ("user_2", "1234")
    ]
    cursor.executemany("""
    INSERT INTO users (username, password)
    VALUES (?, ?)
    """, sample_data)
    
    conn.commit()
    conn.close()
    print("Database initialized and sample data added.")

if __name__ == "__main__":
    init_db()
