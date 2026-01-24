import math
import random

# ----------------------------------
# Synthetic Data (Binary)
# ----------------------------------
X = list(range(1, 21))
y = [1 if x > 10 else 0 for x in X]  # Simple threshold classification

# ----------------------------------
# Initialize Parameters
# ----------------------------------
w = random.uniform(-1, 1)
b = random.uniform(-1, 1)
learning_rate = 0.1
epochs = 1000

# ----------------------------------
# Sigmoid Function
# ----------------------------------
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

# ----------------------------------
# Training Loop
# ----------------------------------
n = len(X)

for epoch in range(epochs):
    dw = 0
    db = 0
    loss = 0

    for x_i, y_i in zip(X, y):
        z = w * x_i + b
        y_pred = sigmoid(z)

        loss += -(y_i * math.log(y_pred + 1e-9) + (1 - y_i) * math.log(1 - y_pred + 1e-9))

        dw += (y_pred - y_i) * x_i
        db += (y_pred - y_i)

    dw /= n
    db /= n
    loss /= n

    w -= learning_rate * dw
    b -= learning_rate * db

    if epoch % 100 == 0:
        print(f"Epoch {epoch}: Loss = {loss:.4f}")

# ----------------------------------
# Final Prediction
# ----------------------------------
print("\nFinal Model Parameters")
print(f"w = {w:.2f}, b = {b:.2f}")

print("\nPredictions:")
for x in [5, 10, 15, 20]:
    prob = sigmoid(w * x + b)
    label = 1 if prob >= 0.5 else 0
    print(f"x = {x}, probability = {prob:.2f}, class = {label}")
