from loss_functions import mse, mae, binary_cross_entropy

y_true = [1, 0, 1, 1]
y_pred = [0.9, 0.1, 0.8, 0.6]

print("MSE:", mse(y_true, y_pred))
print("MAE:", mae(y_true, y_pred))
print("Binary Cross Entropy:", binary_cross_entropy(y_true, y_pred))
