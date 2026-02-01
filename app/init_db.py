from app.database import get_connection

def init():
    db = get_connection()
    cur = db.cursor()

    # Customers table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        phone TEXT
    )
    """)

    # Rooms table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS rooms (
        type TEXT PRIMARY KEY,
        cost INTEGER,
        available INTEGER
    )
    """)

    # Bookings table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT,
        room_type TEXT,
        quantity INTEGER
    )
    """)

    # Bills table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer TEXT UNIQUE,
        total INTEGER
    )
    """)

    # Users table (login system)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    # Default admin account
    cur.execute("""
    INSERT OR IGNORE INTO users (username, password)
    VALUES ('admin', 'admin123')
    """)

    # Seed room data
    cur.execute("""
    INSERT OR IGNORE INTO rooms VALUES
    ('Single', 1500, 10),
    ('Double', 2500, 8),
    ('Suite', 6000, 3)
    """)

    db.commit()
    db.close()


if __name__ == "__main__":
    init()
