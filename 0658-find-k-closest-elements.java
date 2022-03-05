class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        // sliding window = arr[mid:mid+k-1]
        int left = 0;
        int right = arr.length - k;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (x - arr[mid] <= arr[mid + k] - x) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            result.add(arr[left + i]);
        }
        return result;
    }
}