class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        int[] map = new int[1001];
        for (int num : nums1) {
            map[num]++;
        }

        List<Integer> resultList = new ArrayList<>();
        for (int num : nums2) {
            if (map[num]-- > 0) {
                resultList.add(num);
            }
        }

        int[] resultArray = new int[resultList.size()];
        for (int i = 0; i < resultList.size(); i++) {
            resultArray[i] = resultList.get(i);
        }
        return resultArray;
    }
}