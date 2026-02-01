from flask import Flask, render_template, request, redirect, session
from app.database import get_connection
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pw = request.form["password"]

        db = get_connection()
        account = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (user, pw)
        ).fetchone()
        db.close()

        if account:
            session["user"] = user
            return redirect("/")
        else:
            return render_template("login.html", error="Invalid login")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")

    db = get_connection()
    rooms = db.execute("SELECT * FROM rooms").fetchall()
    bills = db.execute("SELECT * FROM bills").fetchall()
    db.close()

    return render_template("index.html", rooms=rooms, bills=bills)


@app.route("/add_customer", methods=["POST"])
def add_customer():
    if "user" not in session:
        return redirect("/login")

    name = request.form["name"]
    address = request.form["address"]
    phone = request.form["phone"]

    db = get_connection()
    db.execute(
        "INSERT INTO customers (name, address, phone) VALUES (?, ?, ?)",
        (name, address, phone),
    )
    db.commit()
    db.close()

    return redirect("/")


@app.route("/book", methods=["POST"])
def book():
    if "user" not in session:
        return redirect("/login")

    customer = request.form["customer"]
    room_type = request.form["room"]
    qty = int(request.form["qty"])

    db = get_connection()

    room = db.execute(
        "SELECT cost, available FROM rooms WHERE type=?",
        (room_type,)
    ).fetchone()

    if room and room["available"] >= qty:
        total_cost = room["cost"] * qty

        db.execute(
            "INSERT INTO bookings (customer, room_type, quantity) VALUES (?, ?, ?)",
            (customer, room_type, qty)
        )

        db.execute(
            "UPDATE rooms SET available = available - ? WHERE type=?",
            (qty, room_type)
        )

        existing = db.execute(
            "SELECT total FROM bills WHERE customer=?",
            (customer,)
        ).fetchone()

        if existing:
            db.execute(
                "UPDATE bills SET total = total + ? WHERE customer=?",
                (total_cost, customer)
            )
        else:
            db.execute(
                "INSERT INTO bills (customer, total) VALUES (?, ?)",
                (customer, total_cost)
            )

        db.commit()

    db.close()
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
