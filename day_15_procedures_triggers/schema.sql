CREATE DATABASE IF NOT EXISTS bank_db;
USE bank_db;

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    name VARCHAR(50),
    balance INT
);

CREATE TABLE transactions (
    tx_id INT AUTO_INCREMENT PRIMARY KEY,
    from_account INT,
    to_account INT,
    amount INT,
    tx_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
