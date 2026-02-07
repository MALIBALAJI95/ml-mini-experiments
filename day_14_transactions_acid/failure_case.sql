START TRANSACTION;

UPDATE accounts
SET balance = balance - 5000
WHERE account_id = 1;

-- Error happens here
UPDATE accounts
SET balance = balance + 'abc'
WHERE account_id = 2;

ROLLBACK;
