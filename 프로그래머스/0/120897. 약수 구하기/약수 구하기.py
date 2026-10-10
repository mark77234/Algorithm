def solution(n):
    answer = []
    
    for i in range(1,n+1): # 0~n
        if n % i == 0:
            answer.append(i)
        
    
    return answer