class Solution {
    public int solution(int n) {
        String str = "";
        
        while (n > 0){
            str += n % 3;
            n /= 3;
        }
        System.out.println(str);
        return Integer.parseInt(str,3);
    }
}