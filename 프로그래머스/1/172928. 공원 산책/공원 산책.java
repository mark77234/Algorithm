import java.util.*;
class Solution {
    public int[] solution(String[] park, String[] routes) {
        int x = 0;
        int y = 0;
        for (int i = 0; i < park.length; i++){
            for (int j = 0; j < park[0].length();j++){
                if (park[i].charAt(j) == 'S'){
                    x = j;
                    y = i;
                    break;
                }
            }
        }
        
        
        for(String route: routes){
            char[] arr = route.toCharArray();
            char point = arr[0];
            int dis = Character.getNumericValue(arr[2]);
            
            int i = 0;
            
            int nx = x;
            int ny = y;
            
            boolean canMove = true;
            
            while (i < dis){
                i++;
                
                if (point == 'E') nx += 1;
                else if (point == 'W') nx -= 1;
                else if (point == 'N') ny -= 1;
                else if (point == 'S') ny += 1;
                
                if ( nx < 0 || ny < 0 || nx >= park[0].length() || ny >= park.length || park[ny].charAt(nx) == 'X' )
                {
                    canMove = false;
                    break;
                }
                
            }
            
            if (canMove){
                x = nx;
                y = ny;
            }
        }
        
        return new int[] {y,x};
    }
}