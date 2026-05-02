def solution(n):
    cnt = 1
    while n > 7:
        n -= 7
        cnt +=1
    
    return cnt