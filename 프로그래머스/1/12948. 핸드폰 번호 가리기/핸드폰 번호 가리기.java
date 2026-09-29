import java.util.*;
class Solution {
    public String solution(String phone_number) {
        String end = phone_number.substring(phone_number.length()-4);
        String start = "*".repeat(phone_number.length()-4);
        System.out.println(start);
        System.out.println(end);
        return start + end;
    }
}