def solution(alp, cop, problems):
    INF = float('inf')
    max_alp =0
    max_cop =0
    
    for p in problems:
        max_alp = max(max_alp,p[0])
        max_cop = max(max_cop,p[1])
    
    
    dp = [[INF] * (max_cop+1) for _ in range(max_alp+1)]
    
    alp = min(alp,max_alp)
    cop = min(cop,max_cop)
    dp[alp][cop] = 0
    
    for i in range(alp,max_alp+1):
        for j in range(cop,max_cop+1):
            if i+1 <= max_alp:
                dp[i+1][j]  = min(dp[i+1][j],dp[i][j]+1)
            if j+1 <= max_cop:
                dp[i][j+1]  = min(dp[i][j+1],dp[i][j]+1)
            
            
            for p in problems:
                alp_req = p[0]
                cop_req = p[1]
                alp_rwd = p[2]
                cop_rwd = p[3]
                cost = p[4]
                
                # 넘어가는거 방지 
                if i >= alp_req and j >= cop_req:
                    next_alp,next_cop = min(i+alp_rwd,max_alp),min(j+cop_rwd,max_cop)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop],cost + dp[i][j])
            
    
    return dp[-1][-1]
    