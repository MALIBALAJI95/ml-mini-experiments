INSERT INTO accounts VALUES (1, 'Rahul', 10000);
INSERT INTO accounts VALUES (2, 'Anita', 8000);

CALL transfer_money(1, 2, 3000);

SELECT * FROM accounts;
SELECT * FROM transactions;
