import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        Map<String,HashSet<String>> reports = new HashMap<>();
        
        Map<String,Integer> mailCount = new HashMap<>();
        
        for(String id: id_list){
            reports.put(id,new HashSet<>());
            mailCount.put(id,0);
        }
        
        
        for (String rep: report){
            String[] r = rep.split(" ");
            reports.get(r[1]).add(r[0]);
            
        }
        
        for (String reported: reports.keySet()){
            HashSet<String> reporters = reports.get(reported);
            
            if (reporters.size() >= k){
                for (String reporter: reporters){
                    mailCount.put(reporter,mailCount.get(reporter) + 1);
                }
            }
        }
        
        List<Integer> result = new ArrayList<>();
        
        for (String id: id_list){
            result.add(mailCount.get(id));
        }
        
        System.out.println(result);
        
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}