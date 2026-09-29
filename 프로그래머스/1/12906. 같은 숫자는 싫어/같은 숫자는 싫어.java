import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        Stack<Integer> stack = new Stack<>();
        
        for (int a: arr){
            if (!stack.isEmpty() && stack.peek() == a){
                continue;
            }
            else{
                stack.push(a);
            }
        }
        
        return stack.stream().mapToInt(Integer::intValue).toArray();
    }
}