import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# ----------------------------------
# 1. Load Dataset
# ----------------------------------
data = pd.read_csv("data/Airbnb_Open_Data.csv")

selected_columns = [
    "price",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
    "availability_365",
    "calculated_host_listings_count"
]

data = data[selected_columns]

# Clean price column
data["price"] = (
    data["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

data["price"] = pd.to_numeric(data["price"], errors="coerce")
data.dropna(inplace=True)

X = data.drop("price", axis=1)
y = data["price"]

# ----------------------------------
# 2. Train-Test Split
# ----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------
# 3. Feature Scaling
# ----------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ----------------------------------
# 4. Helper Function
# ----------------------------------
def evaluate_model(model, X_tr, X_te, y_tr, y_te):
    model.fit(X_tr, y_tr)
    train_pred = model.predict(X_tr)
    test_pred = model.predict(X_te)

    train_rmse = np.sqrt(mean_squared_error(y_tr, train_pred))
    test_rmse = np.sqrt(mean_squared_error(y_te, test_pred))

    return train_rmse, test_rmse

# ----------------------------------
# 5. Linear Regression
# ----------------------------------
linear_model = LinearRegression()
lin_train_rmse, lin_test_rmse = evaluate_model(
    linear_model,
    X_train_scaled,
    X_test_scaled,
    y_train,
    y_test
)

# ----------------------------------
# 6. Polynomial Regression (Degree 2)
# ----------------------------------
poly2 = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly2 = poly2.fit_transform(X_train_scaled)
X_test_poly2 = poly2.transform(X_test_scaled)

poly2_model = LinearRegression()
poly2_train_rmse, poly2_test_rmse = evaluate_model(
    poly2_model,
    X_train_poly2,
    X_test_poly2,
    y_train,
    y_test
)

# ----------------------------------
# 7. Polynomial Regression (Degree 3)
# ----------------------------------
poly3 = PolynomialFeatures(degree=3, include_bias=False)
X_train_poly3 = poly3.fit_transform(X_train_scaled)
X_test_poly3 = poly3.transform(X_test_scaled)

poly3_model = LinearRegression()
poly3_train_rmse, poly3_test_rmse = evaluate_model(
    poly3_model,
    X_train_poly3,
    X_test_poly3,
    y_train,
    y_test
)

# ----------------------------------
# 8. Results
# ----------------------------------
print("Model Comparison (RMSE)")
print("------------------------")
print(f"Linear Regression       -> Train: {lin_train_rmse:.2f}, Test: {lin_test_rmse:.2f}")
print(f"Polynomial Degree 2     -> Train: {poly2_train_rmse:.2f}, Test: {poly2_test_rmse:.2f}")
print(f"Polynomial Degree 3     -> Train: {poly3_train_rmse:.2f}, Test: {poly3_test_rmse:.2f}")
