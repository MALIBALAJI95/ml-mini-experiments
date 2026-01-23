# Day 04 – Gradient Descent From Scratch

## Project Overview
This project implements the Gradient Descent optimization algorithm from scratch
to fit a simple linear regression model.

The goal is to understand how machine learning models learn parameters internally.

---

## Objective
To minimize prediction error by iteratively updating model parameters using gradients.

---

## Mathematical Formulation
Model:
y = wx + b

Loss function:
Mean Squared Error (MSE)

Gradient update rules:
w = w - α * dL/dw  
b = b - α * dL/db

---

## Implementation Details
1. Generated synthetic data
2. Initialized parameters randomly
3. Computed predictions
4. Calculated gradients manually
5. Updated parameters iteratively
6. Observed loss reduction

---

## Output
The script prints:
- Loss at regular intervals
- Final learned slope and intercept

---

## Why Gradient Descent Matters
- Used in linear regression
- Used in neural networks
- Used in deep learning
- Core of modern AI training

---

## How to Run
```bash
python gradient_descent.py
