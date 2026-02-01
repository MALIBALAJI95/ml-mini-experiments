from queries import add_user, add_listing, book_listing, show_bookings

add_user(1, "Rahul", "rahul@gmail.com")
add_user(2, "Anita", "anita@gmail.com")

add_listing(101, "Bangalore", 3000)
add_listing(102, "Goa", 5000)

book_listing(1001, 1, 101)
book_listing(1002, 2, 102)

bookings = show_bookings()

for b in bookings:
    print("User:", b[0], "| Location:", b[1], "| Price:", b[2])
