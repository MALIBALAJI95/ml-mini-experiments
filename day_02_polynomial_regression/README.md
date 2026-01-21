# Day 02 – Polynomial Regression & Overfitting (Airbnb Price Prediction)

## Project Overview
This project demonstrates the concept of **underfitting and overfitting** by comparing
Linear Regression with Polynomial Regression models of different degrees using a
real-world Airbnb dataset.

The goal is to understand how **increasing model complexity** impacts performance on
training and unseen test data.

---

## Problem Statement
Given Airbnb listing details, predict the **price of a listing** using numerical features
and analyze how different regression models behave.

---

## Dataset
**Airbnb Open Dataset**

The dataset contains real-world information about Airbnb listings such as:
- Number of reviews
- Availability
- Minimum nights
- Host listing count
- Price (target variable)

This dataset includes missing values and noisy data, making it suitable for
real-world machine learning practice.

---

## Target Variable
- `price` → Listing price (regression target)

---

## Features Used
The following numerical features were selected:

| Feature | Description |
|--------|------------|
| minimum_nights | Minimum nights required for booking |
| number_of_reviews | Total number of reviews |
| reviews_per_month | Average monthly reviews |
| availability_365 | Days available in a year |
| calculated_host_listings_count | Number of listings by host |

---

## Models Implemented
Three models were trained and compared:

1. **Linear Regression**
2. **Polynomial Regression (Degree 2)**
3. **Polynomial Regression (Degree 3)**

---

## Methodology
The following machine learning pipeline was followed:

1. Loaded Airbnb dataset
2. Selected relevant numerical features
3. Cleaned and converted price column
4. Handled missing values
5. Applied train-test split (80–20)
6. Scaled features using StandardScaler
7. Generated polynomial features
8. Trained regression models
9. Evaluated models using RMSE

---

## Evaluation Metric
Root Mean Squared Error (RMSE) was used to evaluate model performance.

RMSE represents the **average prediction error in price units**.

Lower RMSE = Better model.

---

## Results & Observations

| Model | Train RMSE | Test RMSE |
|------|-----------|-----------|
| Linear Regression | Moderate | Moderate |
| Polynomial (Degree 2) | Lower | Lower |
| Polynomial (Degree 3) | Very Low | Higher |

### Interpretation
- Linear Regression shows **underfitting**
- Degree 2 polynomial gives **best generalization**
- Degree 3 polynomial shows **overfitting**

---

## Key Learnings

- Increasing model complexity reduces training error
- Overfitting occurs when test error increases
- Best model is the one that balances bias and variance
- Train vs Test comparison is essential in ML

---

## How to Run the Project

### Step 1: Install dependencies
```bash
pip install -r requirements.txt
python polynomial_regression.py