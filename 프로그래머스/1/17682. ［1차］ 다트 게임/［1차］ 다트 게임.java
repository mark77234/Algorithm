import java.util.*;
class Solution {
    public int solution(String dartResult) {
        int score[] = new int[3];
        char[] arr = dartResult.toCharArray();
        int idx = -1;
        
        for (int i = 0; i < arr.length;i++){
            if (Character.isDigit(arr[i])){
                idx ++;
                
                if (i + 1< arr.length && arr[i] == '1' && arr[i+1] == '0'){
                    score[idx] = 10;
                    i++;
                }
                else{
                    score[idx] = Character.getNumericValue(arr[i]);
                }
            }
            
            else{
                if (arr[i] == 'S'){
                    score[idx] = (int) Math.pow(score[idx],1);
                }
                else if (arr[i] == 'D'){
                    score[idx] = (int) Math.pow(score[idx],2);
                }
                else if (arr[i] == 'T'){
                    score[idx] = (int) Math.pow(score[idx],3);
                }
                else if (arr[i] == '*'){
                    score[idx] *= 2;
                    if (idx > 0){
                        score[idx - 1] *= 2;
                    }
                }
                else if (arr[i] == '#'){
                    score[idx] *= -1;
                }
            }
                
            }
            
        int total = 0;
        
        for (int s: score){
            total += s;
        }
        return total;
            
        
    }
}