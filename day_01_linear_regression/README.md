# Day 01 – Linear Regression on Airbnb Data

## Objective
Build an end-to-end Linear Regression model to predict Airbnb listing prices using real-world data.

## Dataset
Airbnb Open Dataset containing listing details such as availability, reviews, and minimum nights.

## Target Variable
- `price`

## Features Used
- minimum_nights
- number_of_reviews
- reviews_per_month
- availability_365
- calculated_host_listings_count

## Steps Followed
1. Loaded real Airbnb dataset
2. Selected relevant numerical features
3. Cleaned and converted price data
4. Handled missing values
5. Applied train-test split
6. Scaled features using StandardScaler
7. Trained Linear Regression model
8. Evaluated using MSE, RMSE, and R²
9. Analyzed feature coefficients

## Results
- RMSE shows average error in price prediction
- R² indicates how well listing features explain price variance

## Key Learnings
- Real-world datasets require cleaning before modeling
- Linear Regression provides interpretable coefficients
- Feature scaling improves numerical stability

## How to Run
```bash
pip install -r requirements.txt
python linear_regression.py
