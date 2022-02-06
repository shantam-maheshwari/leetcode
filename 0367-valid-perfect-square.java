class Solution {
    public boolean isPerfectSquare(int num) {
        int left = 1;
        int right = num;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (mid < num / mid) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left * left == num;
    }
}