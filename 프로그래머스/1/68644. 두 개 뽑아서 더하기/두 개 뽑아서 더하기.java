import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < numbers.length; i++){
            for (int j = i +1; j < numbers.length;j++){
                
                int sum = numbers[i]+numbers[j];
                if (answer.contains(sum)){
                    continue;
                }
                answer.add(numbers[i]+numbers[j]);
            }
        }
        
        return answer.stream().sorted().mapToInt(i->i).toArray();
    }
}