import java.util.*;
class Solution {
    public String solution(int[] numbers, String hand) {
        int right = 12;
        int left = 10;
        String answer = "";
        
        for (int n: numbers){
            if (n == 1 || n == 4 || n == 7){
                answer += "L";
                left = n;
            }
            else if (n == 3 || n == 6 || n == 9){
                answer += "R";
                right = n;
            }
            else{
                if (n == 0) n = 11;
                
                int ldis = Math.abs(n - left) / 3 + Math.abs(n-left) % 3;
                int rdis = Math.abs(n - right) / 3 + Math.abs(n-right) % 3;
                
                if (ldis < rdis){
                    answer += "L";
                    left = n;
                }
                else if (rdis < ldis){
                    answer += "R";
                    right = n;
                }
                else{
                    if (hand.equals("right")){
                        answer += "R";
                        right = n;
                    }
                    else{
                        answer += "L";
                        left = n;
                    }
                }
            }
        }
        
        return answer;
    }
}