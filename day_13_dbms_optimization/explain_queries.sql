EXPLAIN
SELECT u.name, l.location, l.price
FROM bookings b
JOIN users u ON b.user_id = u.user_id
JOIN listings l ON b.listing_id = l.listing_id
WHERE l.location = 'Bangalore';
