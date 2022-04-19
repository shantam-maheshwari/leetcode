class Solution {
    public void rotate(int[] nums, int k) {
        k %= nums.length;
        if(k == 0){
            return;
        }
        
        reverse(nums, 0, nums.length - 1 - k);
        reverse(nums, nums.length - k, nums.length - 1);
        reverse(nums, 0, nums.length - 1);
    }
    
    public void reverse(int[] nums, int beg, int end){
        while(beg < end){
            int temp = nums[beg];
            nums[beg++] = nums[end];
            nums[end--] = temp;
        }
    }
}