class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> complementToIndex = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int complement = target - nums[i];
            if(complementToIndex.containsKey(nums[i])){
                return new int[]{complementToIndex.get(nums[i]), i};
            }
            complementToIndex.put(complement, i);
        }
        return new int[]{};
    }
}