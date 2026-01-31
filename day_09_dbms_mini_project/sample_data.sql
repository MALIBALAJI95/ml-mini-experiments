INSERT INTO users VALUES
(1, 'Rahul', 'rahul@gmail.com', '9876543210'),
(2, 'Anita', 'anita@gmail.com', '9123456789');

INSERT INTO hosts VALUES
(1, 'Ramesh', 4.5),
(2, 'Suresh', 4.8);

INSERT INTO listings VALUES
(101, 1, 'Bangalore', 2500),
(102, 2, 'Goa', 4000);

INSERT INTO bookings VALUES
(1001, 1, 101, '2025-02-10', '2025-02-12'),
(1002, 2, 102, '2025-02-15', '2025-02-18');

INSERT INTO payments VALUES
(5001, 1001, 5000, '2025-02-01'),
(5002, 1002, 12000, '2025-02-05');
