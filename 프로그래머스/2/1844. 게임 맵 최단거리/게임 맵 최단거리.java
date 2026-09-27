import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int[] dx = {0,0,1,-1};
        int[] dy = {1,-1,0,0};
        
        Queue<int[]> q = new LinkedList<>();
        
        q.add(new int[]{0,0});
        
        while (!q.isEmpty()){
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];
            
            
            
            for (int i = 0; i < 4;i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (0 <= nx && nx < maps.length && 0 <= ny && ny < maps[0].length){
                    if (maps[nx][ny] == 1){
                        maps[nx][ny] = maps[x][y] + 1;    
                        q.add(new int[]{nx,ny});
                    }
                    
                }
            }
        }
        
        for (int[] m: maps){
            System.out.print(Arrays.toString(m)+"\n");
        }
        
        if (maps[maps.length-1][maps[0].length-1] == 1){
            return -1;
        }
        return maps[maps.length-1][maps[0].length-1];
        
    }
}