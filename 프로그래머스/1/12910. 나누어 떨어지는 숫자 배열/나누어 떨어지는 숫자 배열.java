import java.util.*;
class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> list = new ArrayList<>();
        
        for (int a: arr){
            if (a % divisor == 0){
                list.add(a);
            }
        }
        if (list.isEmpty()){
            return new int[]{-1};
        }
        Collections.sort(list);
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}