from collections import deque

N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]
dfs_visited= [False] * (N+1)
bfs_visited= [False] * (N+1)
dfs_result = []
bfs_result = []

def dfs(v):
    dfs_visited[v] = True
    
    dfs_result.append(v)
    
    for next in graph[v]:
        if not dfs_visited[next]:
            dfs(next)

def bfs(start):
    q = deque([start])
    bfs_visited[start] = True
    while q:
        v = q.popleft()
        bfs_result.append(v)
        
        for next in graph[v]:
            if not bfs_visited[next]:
                bfs_visited[next] = True
                q.append(next)
    
    

for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()
    

dfs(V)
bfs(V)


print(*dfs_result)
print(*bfs_result)