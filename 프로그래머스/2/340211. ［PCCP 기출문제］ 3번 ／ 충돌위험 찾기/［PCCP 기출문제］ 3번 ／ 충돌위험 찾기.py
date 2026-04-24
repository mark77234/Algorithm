# 자동 운송 시스템
# 1. (r,c)와 같이 2차원 좌표로 나타낼 수 있는 n개의 포인트 존재 (1~n까지의 서로 다른 번호)
# 2. 로봇마다 정해진 운송 경로 존재. m개의 포인트로 구성. 첫 포인트부터 할당된 포인트를 순서대로 방문
# 3. 운송 시스템에 사용되는 로봇은 x대이고, 모든 로봇은 0초에 동시에 출발.(로봇은 1초마다 r 좌표와 c 좌표 중 하나가 1만큼 감소하거나 증가한 좌표로 이동할 수 있다.)
# 4. 다음 포인트로 이동할 때는 항상 최단 경로로 이동. 여러가지일 경우, r 좌표가 변하는 이동을 c좌표가 변하는 이동보다 먼저 함.
# 5. 마지막 포인트에 도착한 로봇은 운송을 마치고 물류 센터를 벗어남. 물류센터를 벗어나는 경로는 고려 X

# 이동 중 같은 좌표에 로봇이 2대 이상 모인다면 충돌할 가능성 있는 위험 상황으로 판단.
# 관리자인 당신은 위험한 상황이 몇 번 일어나는지 알고싶음.
# 어떤 시간에 여러 좌표에서 위험 상황이 발생하면 그 횟수 모두 더함

# 운송 포인트 n개
# n개의 좌표를 담은 2차원 정수 배열 points
# 로봇 x대의 운송 경로를 담은 routes

# 위험 상황 횟수 return

# 2 <= points <= 100
# points[i]는 i+1번 포인트의 [r,c] 좌표를 나타내는 길이가 2인 정수 배열

# 2 <= routes의 길이 = 로봇의 수(x) <= 100
# 로봇의 운송 경로, 길이는 모두 같음
# routes[i]는 i+1번째 로봇의 운송경로
# routes[i][j]는 i+1번째 로봇이 j+1번째로 방문하는 포인트 번호
from collections import defaultdict,Counter

def solution(points, routes):
    dict = defaultdict(list)
    answer = 0
    
    for route in routes: # 모든 루트
        start = route[0] # 루트의 첫번째 시작번호
        x,y = points[start-1] # 시작 x,y 좌표
        number = 0
        dict[number].append((x,y))
        
        for i in range(1,len(route)): # 나머지 남은 좌표
            end = route[i] # 도착번호
            end_x,end_y = points[end-1] # 도착 x,y 좌표
            
            while x != end_x: # x 좌표가 다를 경우
                if x < end_x: # x 좌표가 도착좌표보다 크면
                    x += 1
                else: # 작으면
                    x -= 1
                number += 1 # 움직였으니까 +1
                dict[number].append((x,y)) # 딕셔너리 해당 인덱스 번호에 추가(나중에 겹치는거 세줄거)
            
            while y != end_y: # y 좌표 마찬가지
                if y < end_y:
                    y += 1
                else:
                    y -= 1
                
                number += 1
                dict[number].append((x,y))
                
    
    for key in dict:
        count = Counter(dict[key])
        for key in count:
            
            if count[key] > 1:
                answer += 1
    return answer
    