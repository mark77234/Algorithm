import java.util.*;
class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> answer = new ArrayList<>();
        Map<String,Integer> terms_map = new HashMap<>();
        
        
        for (String term: terms){
            String[] t = term.split(" ");
            String term_type = t[0];
            int term_month = Integer.parseInt(t[1]);
            terms_map.put(term_type,term_month);
            
        }
        
        int idx = 0;
        for (String privacy: privacies){
            idx++;
            String[] p = privacy.split(" ");
            String privacy_date = p[0];
            String privacy_term = p[1];
            
            int p_day = getDate(privacy_date) + terms_map.get(privacy_term) * 28;
            
            if (p_day <= getDate(today)){
                answer.add(idx);
            }
            
            
        }
        
        int[] result = new int[answer.size()];
        
        for(int i = 0;i < answer.size();i++){
            result[i] = answer.get(i);
        }
        
        return result;
    }
    
    public static int getDate(String date){
        String[] arr = date.split("\\.");
        int year = Integer.parseInt(arr[0]);
        int month = Integer.parseInt(arr[1]);
        int day = Integer.parseInt(arr[2]);
        
        return (year * 28 * 12) + (month * 28) + day;
    }
}