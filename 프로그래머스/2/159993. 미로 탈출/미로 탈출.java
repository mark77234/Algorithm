import java.util.*;
class Solution {
    public int solution(String[] maps) {
        int[] start = new int[2];
        int[] lever = new int[2];
        int[] exit = new int[2];
        
        for (int i= 0 ; i < maps.length; i++){
            for (int j = 0; j < maps[0].length();j++){
                if (maps[i].charAt(j) == 'S'){
                    start[0] = i;
                    start[1] = j;
                }
                else if (maps[i].charAt(j) == 'L'){
                    lever[0] = i;
                    lever[1] = j;
                }
                else if (maps[i].charAt(j) == 'E'){
                    exit[0] = i;
                    exit[1] = j;
                }
            }
        }
        
        int a = bfs(maps,start,lever);
        if (a == -1){
            return -1;
        }
        int b = bfs(maps,lever,exit);
        
        if (b == -1){
            return -1;
        }
        return a+b;
    }
    
    public static int bfs(String[] maps, int[] start, int[] end){
        int[] dx = {0,0,1,-1};
        int[] dy = {1,-1,0,0};
        
        Queue<int[]> q = new LinkedList<>();
        int[][] visited = new int[maps.length][maps[0].length()];
        
        q.add(new int[]{start[0],start[1]});
        
        while (!q.isEmpty()){
            int[] cur = q.poll();
            
            int x = cur[0];
            int y = cur[1];
            
            if (x == end[0] && y == end[1]){
                return visited[x][y];
            }
            
            for (int i= 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx <0 || nx >= maps.length || ny <0 || ny >= maps[0].length() || maps[nx].charAt(ny) ==  'X' || visited[nx][ny] > 0 ){
                    continue;
                }
                
                visited[nx][ny] = visited[x][y] + 1;
                q.add(new int[]{nx,ny});
            }
        }
        return -1;
    }
}