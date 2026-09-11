
def solution(n):
    answer = [[0 for j in range(1,i+1)] for i in range(1,n+1)]
    
    x= -1
    y = 0
    num = 1
    
    for i in range(n):
        for j in range(i,n): # n-i번 반복
            # 하 -> 우 -> 상 으로 반복되기때문에 
            if i % 3 == 0: # 하 방향일 경우
                x += 1
            elif i % 3 == 1: # 우 방향일 경우
                y += 1
            else:
                x -= 1
                y -= 1
            
            answer[x][y] = num
            num += 1
    
    return sum(answer,[])
                
    
    