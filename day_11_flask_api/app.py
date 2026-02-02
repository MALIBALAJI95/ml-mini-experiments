from flask import Flask, request, jsonify
from db_config import get_connection

app = Flask(__name__)

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users VALUES (%s,%s,%s)",
                   (data["user_id"], data["name"], data["email"]))
    db.commit()
    db.close()
    return jsonify({"message": "User added successfully"})

@app.route("/add_listing", methods=["POST"])
def add_listing():
    data = request.json
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO listings VALUES (%s,%s,%s)",
                   (data["listing_id"], data["location"], data["price"]))
    db.commit()
    db.close()
    return jsonify({"message": "Listing added successfully"})

@app.route("/book", methods=["POST"])
def book():
    data = request.json
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO bookings VALUES (%s,%s,%s)",
                   (data["booking_id"], data["user_id"], data["listing_id"]))
    db.commit()
    db.close()
    return jsonify({"message": "Booking successful"})

@app.route("/bookings", methods=["GET"])
def get_bookings():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT u.name, l.location, l.price
        FROM bookings b
        JOIN users u ON b.user_id = u.user_id
        JOIN listings l ON b.listing_id = l.listing_id
    """)
    data = cursor.fetchall()
    db.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
