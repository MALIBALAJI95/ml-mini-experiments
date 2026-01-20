# Day 02 – Polynomial Regression & Overfitting (Airbnb Data)

## Objective
Demonstrate underfitting and overfitting by increasing model complexity using Polynomial Regression.

## Dataset
Airbnb Open Dataset with real listing and pricing information.

## Target Variable
- `price`

## Models Compared
- Linear Regression
- Polynomial Regression (Degree 2)
- Polynomial Regression (Degree 3)

## Methodology
1. Cleaned real-world Airbnb price data
2. Applied train-test split
3. Standardized features
4. Trained models with increasing complexity
5. Compared Train vs Test RMSE

## Observations
- Linear Regression may underfit complex relationships
- Degree 2 polynomial improves performance
- Degree 3 polynomial reduces training error but increases test error (overfitting)

## Key Learnings
- Higher model complexity is not always better
- Overfitting occurs when a model memorizes training data
- Train-test error comparison is essential

## How to Run
```bash
pip install -r requirements.txt
python polynomial_regression.py
