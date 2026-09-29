class Solution {
    public int solution(int n) {
        int answer = 0;
        
        while (n > 0){
            int a = n % 10;
            
            answer += a;
            
            n = n / 10;
            
        }
        
        return answer;
    }
}