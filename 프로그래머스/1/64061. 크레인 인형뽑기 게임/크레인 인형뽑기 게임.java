import java.util.*;
class Solution {
    public int solution(int[][] board, int[] moves) {
        List<Integer> stack = new ArrayList<>();
        int cnt = 0;
        
        for (int[] b: board){
            System.out.print(Arrays.toString(b)+"\n");
        }
        
        for (int m : moves){
            for (int i=0; i < board.length;i++){
              if (board[i][m-1] != 0){
                  int doll = board[i][m-1];
                  board[i][m-1] = 0;
                  
                  
                  if (!stack.isEmpty() && stack.get(stack.size()-1) == doll){
                      stack.remove(stack.size()-1);
                      cnt += 2;
                  }
                  else{
                      stack.add(doll);
                  }
                  
                  break;
              }
            }   
            
        }
        
        
        
        return cnt;
        
        
        
    }
}