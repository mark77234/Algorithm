from collections import deque

def bfs(maps):
    
    q = deque([(0,0)])
    dx = [1,-1,0,0]
    dy = [0,0,-1,1]
    
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx <len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1 :
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))
    
    for i in maps:
        print(i)
    
    return maps[-1][-1]

    
    

def solution(maps):
    answer = bfs(maps)
    
    if answer > 1:
        return answer
    else:
        return -1
    