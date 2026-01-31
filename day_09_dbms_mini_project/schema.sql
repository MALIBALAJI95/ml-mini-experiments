CREATE DATABASE airbnb_db;
USE airbnb_db;

CREATE TABLE users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    phone VARCHAR(15)
);

CREATE TABLE hosts (
    host_id INT PRIMARY KEY,
    name VARCHAR(50),
    rating FLOAT
);

CREATE TABLE listings (
    listing_id INT PRIMARY KEY,
    host_id INT,
    location VARCHAR(100),
    price_per_night INT,
    FOREIGN KEY (host_id) REFERENCES hosts(host_id)
);

CREATE TABLE bookings (
    booking_id INT PRIMARY KEY,
    user_id INT,
    listing_id INT,
    check_in DATE,
    check_out DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (listing_id) REFERENCES listings(listing_id)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    booking_id INT,
    amount INT,
    payment_date DATE,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);
