CREATE TABLE hosts (
    host_id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE listings (
    listing_id INT PRIMARY KEY,
    location VARCHAR(100),
    price INT,
    host_id INT
);

CREATE TABLE bookings (
    booking_id INT PRIMARY KEY,
    user_id INT,
    listing_id INT
);
