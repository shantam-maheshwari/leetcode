class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] row = new boolean[9][9];
        boolean[][] col = new boolean[9][9];
        boolean[][] box = new boolean[9][9];
        
        for(int i = 0; i < 9; i++){
            for(int j = 0; j < 9; j++){
                char c = board[i][j];
                
                if(c == '.'){
                    continue;
                }
                
                int digit = c - '1';
                if(row[i][digit] || col[j][digit] || box[i/3*3 + j/3][digit]){
                    return false;
                }
                else{
                    row[i][digit] = col[j][digit] = box[i/3*3 + j/3][digit] = true;
                }
            }
        }
        return true;
    }
}