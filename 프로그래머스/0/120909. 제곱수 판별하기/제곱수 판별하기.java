import java.util.*;
class Solution {
    public int solution(int n) {
        
        for (int i = 0; i < n; i++){
            if (n == Math.pow(i,2) ){
                return 1;
            }
        }
        return 2;
    }
}