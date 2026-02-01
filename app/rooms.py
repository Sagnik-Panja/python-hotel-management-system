from app.database import get_connection

def get_room(room_type):
    db = get_connection()
    cur = db.cursor()
    cur.execute("SELECT Cost, Available FROM rooms WHERE Roomtype=%s", (room_type,))
    return cur.fetchone()
