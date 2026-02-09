DELIMITER //

CREATE PROCEDURE transfer_money(
    IN fromAcc INT,
    IN toAcc INT,
    IN amt INT
)
BEGIN
    START TRANSACTION;

    UPDATE accounts
    SET balance = balance - amt
    WHERE account_id = fromAcc;

    UPDATE accounts
    SET balance = balance + amt
    WHERE account_id = toAcc;

    INSERT INTO transactions(from_account, to_account, amount)
    VALUES (fromAcc, toAcc, amt);

    COMMIT;
END //

DELIMITER ;
