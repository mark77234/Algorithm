# bfs로 한 덩어리의 석유를 찾는다
# 한 덩어리의 석유 값을 기억해놨다가 해당하는 열들에 더해준다
# 예시 1) -> 2의 석유가 7,8 열에 포함돼있으니 7,8열에 미리 더해줌
# 그다음 덩어리 7의 석유가 4,5,6,7에 있으니 각 4,5,6,7열에도 또 더해줌
# 8의 석유는 1,2,3열에 더해줌
# 그럼 그 값들을 result 배열의 인덱스에 저장해둠
# result의 max값을 return 하면 됨

from collections import deque

def solution(land):
    n,m = len(land), len(land[0]) # n - 행, m - 열
    visited =[[False]* m for _ in range(n)]
    
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    result = [0]* m
    
    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and visited[y][x] == False:
                q = deque([(x,y)])
                visited[y][x] = True
                oil = 1 # 기름값
                cols = set([x]) # 추가할 열들(중복 제거 set)
                
                while q:
                    cx,cy = q.popleft()
                    
                    for i in range(4):
                        nx = cx + dx[i]
                        ny = cy + dy[i]
                        if 0<= nx < m and 0 <= ny < n:
                            if land[ny][nx] == 1 and visited[ny][nx] == False:
                                cols.add(nx) # 해당 열
                                oil += 1
                                visited[ny][nx] = True
                                q.append((nx,ny))
                    
                for col in cols:
                    result[col] += oil
    
    return max(result)
                                
                        
                        