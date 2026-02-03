CREATE DATABASE IF NOT EXISTS airbnb_db;
USE airbnb_db;

CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS listings (
    listing_id INT PRIMARY KEY,
    location VARCHAR(100),
    price INT
);

CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT PRIMARY KEY,
    user_id INT,
    listing_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (listing_id) REFERENCES listings(listing_id)
);
