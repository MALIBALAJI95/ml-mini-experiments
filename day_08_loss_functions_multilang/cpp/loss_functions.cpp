#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

double mse(vector<double>& yTrue, vector<double>& yPred) {
    double sum = 0;
    for (int i = 0; i < yTrue.size(); i++)
        sum += pow(yTrue[i] - yPred[i], 2);
    return sum / yTrue.size();
}

double mae(vector<double>& yTrue, vector<double>& yPred) {
    double sum = 0;
    for (int i = 0; i < yTrue.size(); i++)
        sum += abs(yTrue[i] - yPred[i]);
    return sum / yTrue.size();
}

double binaryCrossEntropy(vector<double>& yTrue, vector<double>& yPred) {
    double eps = 1e-15;
    double sum = 0;
    for (int i = 0; i < yTrue.size(); i++) {
        double p = min(max(yPred[i], eps), 1 - eps);
        sum += yTrue[i] * log(p) + (1 - yTrue[i]) * log(1 - p);
    }
    return -sum / yTrue.size();
}

int main() {
    vector<double> yTrue = {1, 0, 1, 1};
    vector<double> yPred = {0.9, 0.1, 0.8, 0.6};

    cout << "MSE: " << mse(yTrue, yPred) << endl;
    cout << "MAE: " << mae(yTrue, yPred) << endl;
    cout << "Binary Cross Entropy: " << binaryCrossEntropy(yTrue, yPred) << endl;
}
