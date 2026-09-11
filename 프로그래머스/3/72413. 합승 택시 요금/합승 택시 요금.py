# A,B 각각 최소경로 더하기
# A,B 가는길이 겹치는 간선은 빼주기

# n = 노드 개수, s = 시작 노드, a,b
# fares = c,d,f - 출발,도착,요금
import heapq

def dijkstra(start,n,graph):
    INF = int(1e9)
    distance = [INF] * (n + 1)
    
    q= []
    
    heapq.heappush(q,(0,start))
    
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for next_node, weight in graph[now]:
            cost = dist + weight
            
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q,(cost,next_node))
                
    return distance
    
    

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    answer= int(1e9)
    
    
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    
    s_dist = dijkstra(s,n,graph)
    a_dist = dijkstra(a,n,graph)
    b_dist = dijkstra(b,n,graph)
    
    for i in range(n+1):
        answer= min(answer,s_dist[i]+a_dist[i]+b_dist[i])
    return answer
    
        
    
        
        
        
        
    