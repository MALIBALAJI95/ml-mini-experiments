import random
import numpy as np

# ----------------------------------
# Sample Data (synthetic, no dataset)
# ----------------------------------
X = list(range(1, 21))   # Features
y = [x * 2 + random.randint(-2, 2) for x in X]  # Noisy target

# ----------------------------------
# K-Fold Function
# ----------------------------------
def k_fold_split(X, y, k=5):
    data = list(zip(X, y))
    random.shuffle(data)

    fold_size = len(data) // k
    folds = []

    for i in range(k):
        start = i * fold_size
        end = start + fold_size
        folds.append(data[start:end])

    return folds

# ----------------------------------
# Simple Model (Mean Predictor)
# ----------------------------------
def simple_model(train_data, test_data):
    train_y = [item[1] for item in train_data]
    mean_value = sum(train_y) / len(train_y)

    predictions = [mean_value for _ in test_data]
    actual = [item[1] for item in test_data]

    mse = np.mean([(a - p) ** 2 for a, p in zip(actual, predictions)])
    return mse

# ----------------------------------
# Cross Validation Execution
# ----------------------------------
k = 5
folds = k_fold_split(X, y, k)

mse_scores = []

for i in range(k):
    test_fold = folds[i]
    train_folds = [item for j, fold in enumerate(folds) if j != i for item in fold]

    mse = simple_model(train_folds, test_fold)
    mse_scores.append(mse)

    print(f"Fold {i+1} MSE: {mse:.2f}")

print("\nAverage MSE:", np.mean(mse_scores))
