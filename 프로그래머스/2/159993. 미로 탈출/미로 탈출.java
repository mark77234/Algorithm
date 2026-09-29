import java.util.*;

class Solution {
    public int solution(String[] maps) {
        int answer = -1;
        
        int n = maps.length;
        int m = maps[0].length();
        
        // 시작 지점 
        int[] start = new int[2];
        // 레버 
        int[] lever = new int[2];
        // 출구 
        int[] end = new int[2];
        
        // 시작 지점, 레버, 츨구 좌표 저장 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                char ch = maps[i].charAt(j);
                
                if (ch == 'S') {   
                    start[0] = i;
                    start[1] = j;
                } else if (ch == 'L') { 
                    lever[0] = i;
                    lever[1] = j;
                } else if (ch == 'E') { 
                    end[0] = i;
                    end[1] = j;
                }
            }
        }
        
        int a = bfs(maps, start, lever);
        int b = bfs(maps, lever, end);

        if (a != -1 && b != -1) {
            answer = a + b;
        } 
        
        return answer;
    }
    
    public int bfs(String[] maps, int[] start, int[] end) {     
        int n = maps.length;
        int m = maps[0].length();
        
        // 상, 하, 좌, 우 
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
                
        Queue<int[]> q = new LinkedList<>(); 
		int[][] visited = new int[n][m];   

        int x = start[0];
        int y = start[1];
        
        q.add(new int[]{x, y});

        while(!q.isEmpty()) {
            int[] now = q.poll();
            x = now[0];
            y = now[1];
            
            if (x == end[0] && y == end[1]) {
                return visited[x][y];
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                // 미로의 범위 밖, 벽, 이미 방문한 경우 생략  
                if (nx < 0 || nx >= n || ny < 0 || ny >= m || maps[nx].charAt(ny) == 'X' || visited[nx][ny] > 0) {
                    continue;
                }
                
                // 이동 거리 +1
                visited[nx][ny] = visited[x][y] + 1;    
                q.add(new int[]{nx, ny});
            }
        }
        return -1;
    } 
}