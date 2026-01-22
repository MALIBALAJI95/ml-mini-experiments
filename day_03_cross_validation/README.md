# Day 03 – K-Fold Cross-Validation From Scratch

## Project Overview
This project implements K-Fold Cross-Validation logic manually using pure Python,
without relying on any machine learning libraries or datasets.

The goal is to understand how cross-validation works internally.

---

## Objective
To simulate the process of K-Fold Cross-Validation and evaluate a simple model
across multiple folds.

---

## Key Concepts
- Data shuffling
- Fold creation
- Train-test rotation
- Average error calculation

---

## Implementation Details
1. Synthetic data is generated
2. Data is split into K folds
3. Each fold is used as test set once
4. Remaining folds form training set
5. A simple mean-based model is evaluated
6. MSE is calculated for each fold

---

## Why Cross-Validation Matters
- Reduces evaluation bias
- Uses full dataset effectively
- Provides stable performance estimates
- Essential in real ML systems

---

## Output
The script prints:
- MSE for each fold
- Average MSE across folds

---

## How to Run
```bash
python kfold_from_scratch.py
