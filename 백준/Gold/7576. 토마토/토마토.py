from collections import deque

def bfs():
    
   
    answer = 0
    q = deque()
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                q.append((j,i))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((nx,ny))
                    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return -1
            answer = max(answer,graph[i][j])
    return answer - 1

M,N = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(N)]




print(bfs())



    