class Solution {
    public boolean isPalindrome(String s) {
        int beg = 0;
        int end = s.length() - 1;
        while(beg < end){
            if(!Character.isLetterOrDigit(s.charAt(beg))){
                beg++;
                continue;
            }
            if(!Character.isLetterOrDigit(s.charAt(end))){
                end--;
                continue;
            }
            if(Character.toLowerCase(s.charAt(beg)) != Character.toLowerCase(s.charAt(end))){
                return false;
            }
            beg++;
            end--;
        }
        return true;
    }
}