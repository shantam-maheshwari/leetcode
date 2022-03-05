class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] result = { -1, -1 };
        if (nums == null || nums.length == 0) {
            return result;
        }
        result[0] = binarySearchFirstOccurrence(nums, 0, nums.length - 1, target);
        if (result[0] == -1) {
            return result;
        }
        result[1] = binarySearchLastOccurrence(nums, result[0], nums.length - 1, target);
        return result;
    }

    public int binarySearchFirstOccurrence(int[] nums, int left, int right, int target) {
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left] == target ? left : -1;
    }

    public int binarySearchLastOccurrence(int[] nums, int left, int right, int target) {
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (nums[mid] <= target) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return nums[left] == target ? left : -1;
    }
}