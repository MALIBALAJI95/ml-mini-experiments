import math

# ----------------------------------
# Activation Functions
# ----------------------------------
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(a):
    return a * (1 - a)

def tanh(x):
    return math.tanh(x)

def tanh_derivative(a):
    return 1 - a**2

def relu(x):
    return max(0, x)

def relu_derivative(x):
    return 1 if x > 0 else 0

# ----------------------------------
# Input Values
# ----------------------------------
inputs = [-5, -2, -1, 0, 1, 2, 5]

print("Activation Function Comparison\n")

print("Input | Sigmoid | Tanh | ReLU")
print("--------------------------------")
for x in inputs:
    print(f"{x:>5} | {sigmoid(x):.4f}  | {tanh(x):.4f} | {relu(x):.2f}")

print("\nDerivatives (for learning)")
print("Input | Sigmoid' | Tanh' | ReLU'")
print("-----------------------------------")
for x in inputs:
    s = sigmoid(x)
    t = tanh(x)
    print(f"{x:>5} | {sigmoid_derivative(s):.4f}   | {tanh_derivative(t):.4f} | {relu_derivative(x)}")
