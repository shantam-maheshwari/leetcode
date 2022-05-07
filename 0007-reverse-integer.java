class Solution {
    public int reverse(int x) {
        int xReversed = 0;
        while(x != 0){
            int digit = x%10;
            
            if(xReversed > Integer.MAX_VALUE/10 || (xReversed == Integer.MAX_VALUE/10 && digit > 7)){
                return 0;
            }
            if(xReversed < Integer.MIN_VALUE/10 || (xReversed == Integer.MIN_VALUE/10 && digit < -8)){
                return 0;
            }
            
            xReversed = xReversed*10 + digit;
            x = x/10;
        }
        return xReversed;
    }
}