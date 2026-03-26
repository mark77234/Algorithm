from collections import deque

def bfs(visited,cX,cY,iX,iY):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q = deque([(cX,cY)])
    
    visited[cY][cX] = 1
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(visited) and 0 <= ny < len(visited[0]):
                if visited[ny][nx] == 1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((nx,ny))
    
    return visited[iY][iX]
    

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    max_len = 0
    characterX *=2
    characterY *=2
    itemX *= 2
    itemY *=2
    
    for rect in rectangle:
        max_len = max(max_len,max(rect))
    size = (max_len+1)*2
    
    visited = [[-1]*size for _ in range(size)]
    
    for rect in rectangle:
        x1,y1,x2,y2 = rect[0]*2,rect[1]*2,rect[2]*2,rect[3]*2
        
        
        for i in range(y1,y2+1):
            for j in range(x1,x2+1):
                if y1 < i < y2 and x1 < j < x2:
                    visited[i][j] = 0
                elif visited[i][j] != 0:
                    visited[i][j] = 1
        
        
    return (bfs(visited,characterX,characterY,itemX,itemY) // 2)
   
        