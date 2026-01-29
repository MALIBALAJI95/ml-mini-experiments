public class LossFunctions {

    public static double mse(double[] yTrue, double[] yPred) {
        double sum = 0;
        for (int i = 0; i < yTrue.length; i++) {
            sum += Math.pow(yTrue[i] - yPred[i], 2);
        }
        return sum / yTrue.length;
    }

    public static double mae(double[] yTrue, double[] yPred) {
        double sum = 0;
        for (int i = 0; i < yTrue.length; i++) {
            sum += Math.abs(yTrue[i] - yPred[i]);
        }
        return sum / yTrue.length;
    }

    public static double binaryCrossEntropy(double[] yTrue, double[] yPred) {
        double eps = 1e-15;
        double sum = 0;
        for (int i = 0; i < yTrue.length; i++) {
            double p = Math.min(Math.max(yPred[i], eps), 1 - eps);
            sum += yTrue[i] * Math.log(p) + (1 - yTrue[i]) * Math.log(1 - p);
        }
        return -sum / yTrue.length;
    }

    public static void main(String[] args) {
        double[] yTrue = {1, 0, 1, 1};
        double[] yPred = {0.9, 0.1, 0.8, 0.6};

        System.out.println("MSE: " + mse(yTrue, yPred));
        System.out.println("MAE: " + mae(yTrue, yPred));
        System.out.println("Binary Cross Entropy: " + binaryCrossEntropy(yTrue, yPred));
    }
}
