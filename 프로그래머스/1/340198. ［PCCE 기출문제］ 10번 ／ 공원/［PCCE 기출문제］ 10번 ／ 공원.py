# 돗자리의 한 변의 길이가 5,3,2 세 종류

# 돗자리들의 한 변의 길이들이 담긴 정수 리스트 - mats
# 현재 공원의 자리 배치도를 의미하는 2차원 문자열 리스트 - park
# 지민이가 깔 수 있는 가장 큰 돗자리 한변의 길이 return


def solution(mats, park):
    mats.sort(reverse=True)
    row = len(park)
    col = len(park[0])
    answer = -1
    
    for y in range(row):
        for x in range(col):
            if park[y][x] != "-1":
                continue
            
            for mat in mats:
                if answer >= mat:
                    continue
                
                if y + mat > row or x + mat > col:
                    continue
                    
                possible = True
                
                for i in range(mat):
                    
                    if park[y+i][x:x+mat] != ["-1"] * mat:
                        possible = False
                        break
                
                
                if possible:
                    answer = mat
                    break
                    
                
    return answer
                   

