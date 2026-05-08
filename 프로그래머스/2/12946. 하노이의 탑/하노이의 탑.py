
def solution(n):
    
    def hanoi(start,end,rest,n,answer):
        
        if n == 1: # n이 1이면 이동
            answer.append([start,end])
        
        else:
            hanoi(start,rest,end,n-1,answer) # n-1개를 남는공간으로 옮기기
            hanoi(start,end,rest,1,answer)  # 남는 공간에 다 옮겼으면 제일 큰 판을 end로 옮기기
            hanoi(rest,end,start,n-1,answer)  # 남는 공간에 남아있는 판들 다 옮기기
        
        return answer
    
    
    return hanoi(1,3,2,n,[])