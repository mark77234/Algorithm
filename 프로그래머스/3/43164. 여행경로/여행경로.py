def dfs(tickets,li):
    start_idx = -1
    
    start = li[-1]
    
    if len(tickets) == 0:
        return li
    
    for i in range(len(tickets)):
        if tickets[i][0] == start:
            start_idx = i
            break
            
    
    if start_idx == -1:
        return []
    
    while tickets[start_idx][0] == start:
        next = dfs(tickets[:start_idx]+tickets[start_idx+1:],li + [tickets[start_idx][1]])
    
        if next != []:
            return next
        
        start_idx+=1
    
    return []
    

    
    
    
    

def solution(tickets):
    tickets.sort()
    
    return dfs(tickets,["ICN"])
    
  
    