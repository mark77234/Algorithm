def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    def dfs(i):
        visited[i] = True
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == False:
                dfs(j)
    
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            cnt += 1
        
    return cnt