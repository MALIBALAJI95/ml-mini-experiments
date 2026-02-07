CREATE DATABASE IF NOT EXISTS bank_db;
USE bank_db;

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    name VARCHAR(50),
    balance INT
);
