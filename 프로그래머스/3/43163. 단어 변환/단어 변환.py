from collections import deque

def bfs(begin,target,words):
    
    q = deque([(begin,0)])
    
    while q:
        
        start,cnt = q.popleft()
        if start == target:
            return cnt
        for word in words:
            diff = 0
            for i in range(len(start)):
                if start[i] != word[i]:
                    diff += 1
            
            if diff == 1:
                q.append((word,cnt + 1))
    


def solution(begin, target, words):
    if target not in words:
        return 0
    
    return bfs(begin,target,words)
        
    