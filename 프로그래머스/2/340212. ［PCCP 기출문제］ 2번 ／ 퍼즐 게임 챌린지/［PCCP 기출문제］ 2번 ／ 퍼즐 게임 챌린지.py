# n개의 퍼즐
# 퍼즐의 난이도 diff
# 현재 퍼즐 소요 시간 - time_cur, 이전 - time_prev
# 숙련도 - level
# 난이도 <= 숙련도 -> time_cur 만큼 시간 사용
# 난이도 > 숙련도 -> (난이도 - 숙련도) 번 틀림. 틀릴때마다 현재시간 사용, 추가로 이전시간만큼의 시간을 사용해 이전 퍼즐 풀어야함
# 이전 퍼즐을 다시 풀 때는 이전 퍼즐의 난이도에 상관없이 틀리지 않음.
# 난이도 - 숙련도번 틀린 후 다시 풀면 time_cur만큼 시간 사용

# 첫번째 난이도는 무조건 통과


def solution(diffs, times, limit):
    right = max(diffs) # 난이도의 최댓값 = 숙련도 최댓값
    left = 1
    answer= max(diffs)
    
    while left < right:
        mid = (right + left) // 2
        time = times[0]
        
        for i in range(1,len(diffs)):
            if mid >= diffs[i]:
                time += times[i]
            else:
                incorrect = diffs[i] - mid
                time += (times[i] + times[i-1]) * incorrect + times[i]
            
        if time <= limit:
            right = mid
            answer = mid
        else:
            left = mid + 1
    
    return answer
    
            
        