-- 1. Find all bookings with user names
SELECT u.name, b.booking_id, b.check_in, b.check_out
FROM users u
JOIN bookings b ON u.user_id = b.user_id;

-- 2. Find total revenue generated
SELECT SUM(amount) AS total_revenue FROM payments;

-- 3. Find hosts with their listings
SELECT h.name, l.location, l.price_per_night
FROM hosts h
JOIN listings l ON h.host_id = l.host_id;

-- 4. Find most expensive listing
SELECT location, price_per_night
FROM listings
ORDER BY price_per_night DESC
LIMIT 1;

-- 5. Find bookings in Goa
SELECT b.booking_id, u.name
FROM bookings b
JOIN users u ON b.user_id = u.user_id
JOIN listings l ON b.listing_id = l.listing_id
WHERE l.location = 'Goa';
