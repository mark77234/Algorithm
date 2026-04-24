# 같은 색깔로 칠해진 칸의 개수 구하기

def solution(board, h, w):
    target = board[h][w]
    l = len(board)
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt = 0
    
    for i in range(4):
        nx = w + dx[i]
        ny = h + dy[i]
                    
        if 0 <= nx < l and 0 <= ny < l:
            if board[ny][nx] == target:
                cnt += 1
    return cnt