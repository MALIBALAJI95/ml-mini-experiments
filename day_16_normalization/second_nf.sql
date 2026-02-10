CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(15)
);

CREATE TABLE listings (
    listing_id INT PRIMARY KEY,
    location VARCHAR(100),
    price INT,
    host_name VARCHAR(50)
);

CREATE TABLE bookings (
    booking_id INT,
    user_id INT,
    listing_id INT
);
