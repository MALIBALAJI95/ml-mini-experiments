import math

def mse(y_true, y_pred):
    return sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / len(y_true)

def mae(y_true, y_pred):
    return sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / len(y_true)

def binary_cross_entropy(y_true, y_pred):
    eps = 1e-15
    loss = 0
    for yt, yp in zip(y_true, y_pred):
        yp = min(max(yp, eps), 1 - eps)
        loss += yt * math.log(yp) + (1 - yt) * math.log(1 - yp)
    return -loss / len(y_true)
