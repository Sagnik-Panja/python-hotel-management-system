from app.database import get_connection

def add_customer(data):
    db = get_connection()
    cur = db.cursor()
    cur.execute("""
        INSERT INTO custdata
        (Cid, Custname, Address, Phone, Bill, Indate, Outdate)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """, data)

def list_customers():
    db = get_connection()
    cur = db.cursor()
    cur.execute("SELECT * FROM custdata")
    return cur.fetchall()
