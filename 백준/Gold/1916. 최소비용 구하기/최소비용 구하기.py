import heapq

N = int(input())
M = int(input())

graph= [[] for _ in range(N+1)]

for i in range(M):
    a, b, val= map(int,input().split())
    graph[a].append([b,val])

start, end = map(int,input().split())


distance = [float('inf')] * (N+1)
distance[start] = 0

heap = []
heapq.heappush(heap,(0,start))

while heap:
    cur_dis,cur = heapq.heappop(heap) # 0,1
    if distance[cur] < cur_dis: # ditance[5] = 4 로 이미 정해졌을 때, 또 똑같이 (1->5,val=10)으로 들어오면 무시하고 넘어가기
        continue
    for next,next_dis in graph[cur]:
        sum_dis = next_dis + cur_dis 
        if sum_dis < distance[next]: 
            distance[next] = sum_dis
            heapq.heappush(heap,(sum_dis,next)) 
        
print(distance[end])

