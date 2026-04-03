from collections import deque

def bfs(a,b,graph):
    
    dist = [row[:] for row in graph] # 그래프 복사
    dist[b][a] = 1
    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    
    q = deque([(a,b)])
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0<= nx < len(dist[0]) and 0 <= ny < len(dist):
                if dist[ny][nx] in ("S","O", "L", "E"): 
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((nx,ny))
    return dist

def solution(maps):
    sx = 0
    sy = 0
    ex = 0
    ey = 0
    lx = 0
    ly = 0
    
    maps = [list(m) for m in maps]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                sx = j
                sy = i
            elif maps[i][j] == "E":
                ex = j
                ey = i
            elif maps[i][j] == "L":
                lx = j
                ly = i
    
    dist_s = bfs(sx,sy,maps)
    
    if isinstance(dist_s[ly][lx],str):
        return -1
    
    s_to_l = dist_s[ly][lx] - 1
    
    dist_l = bfs(lx,ly,maps)
    
    if isinstance(dist_l[ey][ex],str):
        return -1
    l_to_e = dist_l[ey][ex] - 1
    return s_to_l +  l_to_e
    
    
    
    