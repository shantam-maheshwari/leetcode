class Solution {
    public int[] searchRange(int[] nums, int target) {
        // result = {firstIndex, lastIndex}
        int[] result = new int[2];
        result[0] = result[1] = -1;
        if (nums == null || nums.length == 0) {
            return result;
        }
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= target) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        if (nums[left] != target) {
            return result;
        }
        result[0] = left;
        right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (nums[mid] <= target) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        result[1] = left;
        return result;
    }
}