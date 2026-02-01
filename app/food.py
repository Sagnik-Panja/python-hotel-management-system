from app.database import get_connection

def get_food(item):
    db = get_connection()
    cur = db.cursor()
    cur.execute("SELECT Cost FROM hotelmenu WHERE Item=%s", (item,))
    return cur.fetchone()
