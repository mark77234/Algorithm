import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        if (arr.length == 1){
            return new int[]{-1};
        }
        int v = arr[0];
        for(int a: arr){
            v = Math.min(v,a);
        }
        
        int[] result = new int[arr.length - 1];
        int idx = 0;
        for (int i=0;i < arr.length ; i++){
            if (arr[i] == v){
                continue;
            }
            result[idx] = arr[i];
            idx ++;
        }
        
        return result;
    }
}