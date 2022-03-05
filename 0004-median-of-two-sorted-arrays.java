class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int length1 = nums1.length;
        int length2 = nums2.length;
        if (length1 > length2) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int leftIndex = 0;
        int rightIndex = length1;
        while (leftIndex <= rightIndex) {
            int cut1 = (leftIndex + rightIndex) / 2;
            int cut2 = (length1 + length2 + 1) / 2 - cut1;

            int left1 = cut1 == 0 ? Integer.MIN_VALUE : nums1[cut1 - 1];
            int right1 = cut1 == length1 ? Integer.MAX_VALUE : nums1[cut1];

            int left2 = cut2 == 0 ? Integer.MIN_VALUE : nums2[cut2 - 1];
            int right2 = cut2 == length2 ? Integer.MAX_VALUE : nums2[cut2];

            if (left1 <= right2 && left2 <= right1) {
                if ((length1 + length2) % 2 == 0) {
                    return ((double) Math.max(left1, left2) + Math.min(right1, right2)) / 2;
                } else {
                    return Math.max(left1, left2);
                }
            } else if (left1 > right2) {
                rightIndex = cut1 - 1;
            } else {
                leftIndex = cut1 + 1;
            }
        }
        return -1;
    }
}