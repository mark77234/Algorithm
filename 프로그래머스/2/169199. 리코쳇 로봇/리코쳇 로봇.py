from collections import deque

def bfs(a, b, graph, row, column):
    q = deque([(a, b)])
    

    while q:
        x, y = q.popleft()

        # 오른쪽
        k = x
        while (k+1) < column and graph[y][k+1] != "D":
            k += 1
        if k != x and graph[y][k] == 0:
            graph[y][k] = graph[y][x] + 1
            q.append((k, y))

        # 왼쪽
        k = x
        while (k-1) >= 0 and graph[y][k-1] != "D":
            k -= 1
        if k != x and graph[y][k] == 0:
            graph[y][k] = graph[y][x] + 1
            q.append((k, y))

        # 아래
        k = y
        while (k+1) < row and graph[k+1][x] != "D":
            k += 1
        if k != y and graph[k][x] == 0:
            graph[k][x] = graph[y][x] + 1
            q.append((x, k))

        # 위
        k = y
        while (k-1) >= 0 and graph[k-1][x] != "D":
            k -= 1
        if k != y and graph[k][x] == 0:
            graph[k][x] = graph[y][x] + 1
            q.append((x, k))


def solution(board):
    row = len(board)
    column = len(board[0])
    graph = [[0]*column for _ in range(row)]
    

    for y in range(row):
        for x in range(column):
            if board[y][x] == "D":
                graph[y][x] = "D"
            elif board[y][x] == "G":
                answer =(x,y)

    for y in range(row):
        for x in range(column):
            if board[y][x] == "R":
                bfs(x, y, graph, row, column)

    gx = answer[0]
    gy = answer[1]
    
    if graph[gy][gx] !=0:
        return graph[gy][gx]
    return -1

