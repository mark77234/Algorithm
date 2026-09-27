import java.util.*;
class Solution {
    public String solution(String new_id) {
            
        new_id = new_id.toLowerCase();
        
        new_id = new_id.replaceAll("[^a-z0-9-_.]","");
        
        while (new_id.contains("..")){
            new_id = new_id.replace("..",".");
        }
        
        if (new_id.length() > 0 && new_id.charAt(0) == '.'){
            new_id = new_id.substring(1);
        }
        if (new_id.length() > 0 && new_id.charAt(new_id.length()-1) == '.'){
            new_id = new_id.substring(0,new_id.length()-1);
        }
        
        if (new_id.length() == 0) new_id = "a";
        
        if (new_id.length() > 15){
            new_id = new_id.substring(0,15);
            if (new_id.endsWith(".")) new_id = new_id.substring(0,new_id.length() - 1);
        }
        
        while (new_id.length() <= 2){
            new_id += String.valueOf(new_id.charAt(new_id.length()-1));
        }
        
        return new_id;
    }
}