import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ----------------------------------
# 1. Load Dataset
# ----------------------------------
data = pd.read_csv("data/Airbnb_Open_Data.csv")

# ----------------------------------
# 2. Select Relevant Columns
# ----------------------------------
# Target: price
# Features chosen based on availability and usefulness
selected_columns = [
    "price",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
    "availability_365",
    "calculated_host_listings_count"
]

data = data[selected_columns]

# ----------------------------------
# 3. Data Cleaning
# ----------------------------------
# Convert price to numeric (remove $ and commas if present)
data["price"] = (
    data["price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

data["price"] = pd.to_numeric(data["price"], errors="coerce")

# Drop rows with missing values
data.dropna(inplace=True)

# ----------------------------------
# 4. Feature-Target Split
# ----------------------------------
X = data.drop("price", axis=1)
y = data["price"]

# ----------------------------------
# 5. Train-Test Split
# ----------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ----------------------------------
# 6. Feature Scaling
# ----------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ----------------------------------
# 7. Model Training
# ----------------------------------
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# ----------------------------------
# 8. Predictions
# ----------------------------------
y_pred = model.predict(X_test_scaled)

# ----------------------------------
# 9. Model Evaluation
# ----------------------------------
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation Results")
print("------------------------")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R2   : {r2:.4f}")

# ----------------------------------
# 10. Feature Importance
# ----------------------------------
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values(by="Coefficient", ascending=False)

print("\nFeature Impact on Price")
print(coefficients)
