import math
import random

# ----------------------------------
# Synthetic Data
# ----------------------------------
X = [i for i in range(1, 21)]
y = [1 if x > 10 else 0 for x in X]  # Binary classification

# ----------------------------------
# Initialize Weights
# ----------------------------------
w1 = random.uniform(-1, 1)
b1 = random.uniform(-1, 1)

w2 = random.uniform(-1, 1)
b2 = random.uniform(-1, 1)

learning_rate = 0.1
epochs = 1000

# ----------------------------------
# Activation Function
# ----------------------------------
def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def sigmoid_derivative(a):
    return a * (1 - a)

# ----------------------------------
# Training
# ----------------------------------
for epoch in range(epochs):
    total_loss = 0

    for x_i, y_i in zip(X, y):
        # Forward pass
        z1 = w1 * x_i + b1
        a1 = sigmoid(z1)

        z2 = w2 * a1 + b2
        y_pred = sigmoid(z2)

        # Loss
        loss = (y_i - y_pred) ** 2
        total_loss += loss

        # Backpropagation
        d_loss_d_ypred = -2 * (y_i - y_pred)

        d_ypred_d_z2 = sigmoid_derivative(y_pred)
        d_z2_d_w2 = a1
        d_z2_d_b2 = 1

        d_z2_d_a1 = w2
        d_a1_d_z1 = sigmoid_derivative(a1)
        d_z1_d_w1 = x_i
        d_z1_d_b1 = 1

        # Gradients
        dw2 = d_loss_d_ypred * d_ypred_d_z2 * d_z2_d_w2
        db2 = d_loss_d_ypred * d_ypred_d_z2 * d_z2_d_b2

        dw1 = d_loss_d_ypred * d_ypred_d_z2 * d_z2_d_a1 * d_a1_d_z1 * d_z1_d_w1
        db1 = d_loss_d_ypred * d_ypred_d_z2 * d_z2_d_a1 * d_a1_d_z1 * d_z1_d_b1

        # Update
        w2 -= learning_rate * dw2
        b2 -= learning_rate * db2
        w1 -= learning_rate * dw1
        b1 -= learning_rate * db1

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {total_loss/len(X):.4f}")

# ----------------------------------
# Final Predictions
# ----------------------------------
print("\nFinal Predictions:")
for x in [5, 10, 15, 20]:
    z1 = w1 * x + b1
    a1 = sigmoid(z1)
    z2 = w2 * a1 + b2
    y_pred = sigmoid(z2)
    print(f"x={x}, predicted={round(y_pred, 3)}")
