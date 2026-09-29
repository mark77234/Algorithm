import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> list = new ArrayList<>();
        
        for (int a: arr){
            if (!list.isEmpty() && list.get(list.size()-1) == a){
                continue;
            }
            else{
                list.add(a);    
            }
            
        }
        
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}