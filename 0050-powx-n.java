class Solution {
    public double myPow(double x, int n) {
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        return pow(x, n);
    }

    public double pow(double x, int n) {
        if (n == 0) {
            return 1;
        }
        double a = pow(x, n / 2);
        return n % 2 == 0 ? a * a : a * a * x;
    }
}