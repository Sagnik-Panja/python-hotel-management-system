import sqlite3
import os

# Database file stored in working directory (Render-safe)
DB_PATH = os.path.join(os.getcwd(), "hotel.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
