# Day 14 – Transactions & ACID Properties

## Overview
This project demonstrates how databases use transactions to ensure
data consistency using ACID properties.

---

## What is ACID?
| Property | Meaning |
|--------|--------|
Atomicity | All or nothing  
Consistency | Data remains valid  
Isolation | Transactions don’t interfere  
Durability | Data is saved permanently  

---

## What This Project Does
- Simulates bank money transfer
- Shows COMMIT and ROLLBACK
- Demonstrates failure recovery

---

## Files
| File | Purpose |
|------|--------|
schema.sql | Account table  
data.sql | Initial balances  
transaction.sql | Successful transfer  
failure_case.sql | Rollback demo  

---

## Why This Matters
Banks, payment apps, and e-commerce systems
all rely on transactions.
