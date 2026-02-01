from db_config import get_connection

def add_user(user_id, name, email):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users VALUES (%s,%s,%s)", (user_id, name, email))
    db.commit()
    db.close()

def add_listing(listing_id, location, price):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO listings VALUES (%s,%s,%s)", (listing_id, location, price))
    db.commit()
    db.close()

def book_listing(booking_id, user_id, listing_id):
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO bookings VALUES (%s,%s,%s)", (booking_id, user_id, listing_id))
    db.commit()
    db.close()

def show_bookings():
    db = get_connection()
    cursor = db.cursor()
    cursor.execute("""
        SELECT u.name, l.location, l.price
        FROM bookings b
        JOIN users u ON b.user_id = u.user_id
        JOIN listings l ON b.listing_id = l.listing_id
    """)
    return cursor.fetchall()
