// Approach 1: find pivot using binary search, then search for target in one half using binary search
// two passes
// O(log(N))
class Solution {
    public int search(int[] nums, int target) {
        int pivot = getPivot(nums);
        if (nums[0] <= target) {
            return binarySearch(nums, target, 0, pivot);
        } else {
            return binarySearch(nums, target, pivot + 1, nums.length - 1);
        }
    }

    public int getPivot(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[mid + 1]) {
                return mid;
            }
            if (nums[mid] >= nums[0]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    // Gotcha: if nums is sorted, pivot = nums.length - 1
    // if nums[0] > target, binarySearch(nums, target, nums.length, nums.length - 1)
    // is called
    // hence, implement binarySearch to handle out of bound indexes
    public int binarySearch(int[] nums, int target, int left, int right) {
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }
}

// Approach 2: search for target using modified binary search
// one pass
// O(log(N))
class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            // nums[left:mid] is sorted
            else if (nums[left] <= nums[mid]) {
                if (nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            // nums[mid:right] is sorted
            else {
                if (nums[mid] < target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return nums[left] == target ? left : -1;
    }
}