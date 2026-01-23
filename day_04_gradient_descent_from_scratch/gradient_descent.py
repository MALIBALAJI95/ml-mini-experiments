import random

# ----------------------------------
# Synthetic Data (No dataset)
# ----------------------------------
X = list(range(1, 21))
y = [2*x + 5 + random.randint(-2, 2) for x in X]  # y = 2x + 5 + noise

# ----------------------------------
# Initialize Parameters
# ----------------------------------
w = random.uniform(0, 1)
b = random.uniform(0, 1)
learning_rate = 0.01
epochs = 1000

# ----------------------------------
# Gradient Descent
# ----------------------------------
n = len(X)

for epoch in range(epochs):
    y_pred = [w*x + b for x in X]

    dw = (-2/n) * sum(x * (y_i - y_p) for x, y_i, y_p in zip(X, y, y_pred))
    db = (-2/n) * sum((y_i - y_p) for y_i, y_p in zip(y, y_pred))

    w = w - learning_rate * dw
    b = b - learning_rate * db

    if epoch % 100 == 0:
        loss = sum((y_i - y_p)**2 for y_i, y_p in zip(y, y_pred)) / n
        print(f"Epoch {epoch}: Loss = {loss:.4f}")

# ----------------------------------
# Final Result
# ----------------------------------
print("\nFinal Learned Parameters")
print(f"w (slope)     = {w:.2f}")
print(f"b (intercept) = {b:.2f}")
