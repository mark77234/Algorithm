from collections import deque

def bfs(a,b):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    q = deque([(a,b)])
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<=nx<M and 0 <= ny < N:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append((nx,ny))
    
            

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())

    graph= [[0]* M for _ in range(N)]
    answer= 0


    for _ in range(K):
        x,y = map(int,input().split())
        graph[y][x] = 1
        

    for b in range(N):
            for a in range(M):
                if graph[b][a] == 1:
                    bfs(a,b)
                    answer +=1 
                    
    print(answer)

