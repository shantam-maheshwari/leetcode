class Solution {
    public int getMaxLen(int[] nums) {
        int maxLen = 0;
        int posLen = 0;
        int negLen = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                posLen = 0;
                negLen = 0;
            } else if (nums[i] > 0) {
                posLen++;
                if (negLen > 0) {
                    negLen++;
                }
            } else {
                int temp = posLen;
                posLen = negLen;
                negLen = temp;

                if (posLen > 0) {
                    posLen++;
                }
                negLen++;
            }
            maxLen = Math.max(maxLen, posLen);
        }
        return maxLen;
    }
}