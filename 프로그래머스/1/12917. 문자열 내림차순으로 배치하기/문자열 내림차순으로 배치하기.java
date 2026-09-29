import java.util.*;
class Solution {
    public String solution(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        System.out.println(arr);
        String answer = new StringBuilder(new String(arr)).reverse().toString();
        return answer;
    }
}