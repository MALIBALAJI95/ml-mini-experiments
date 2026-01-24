# Day 05 – Logistic Regression From Scratch

## Project Overview
This project implements Logistic Regression manually using pure Python to perform
binary classification.

The goal is to understand how classification models learn using gradient descent.

---

## Objective
To predict binary class labels (0 or 1) using the sigmoid function and optimize
parameters using cross-entropy loss.

---

## Mathematical Model
Sigmoid:
p = 1 / (1 + e^-(wx + b))

Loss:
Binary Cross Entropy

Update:
w = w - α * dL/dw  
b = b - α * dL/db

---

## Implementation Details
1. Generated synthetic binary data
2. Initialized parameters
3. Applied sigmoid activation
4. Computed cross-entropy loss
5. Updated parameters using gradients
6. Observed loss reduction

---

## Output
The script prints:
- Loss at regular intervals
- Final model parameters
- Predictions for sample inputs

---

## Why Logistic Regression Matters
- Used in spam detection
- Used in medical diagnosis
- Used in credit scoring
- Foundation of neural networks

---

## How to Run
```bash
python logistic_regression.py
