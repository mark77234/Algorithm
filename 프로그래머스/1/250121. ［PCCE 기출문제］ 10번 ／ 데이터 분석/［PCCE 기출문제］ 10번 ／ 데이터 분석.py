# 데이터 분석 [코드번호(code), 제조일(date),최대 수량(maximum), 현재 수량(remain),]
# 이차원 정수 리스트 - data
# 어떤 정보를 기준으로 뽑아낼지 문자열 - ext
# 뽑아낼 정보의 기준값 - val_ext
# 정보를 정렬할 기준 문자열 - sort_by

# data에서 ext값이 val_ext보다 작은 데이터만 뽑은 후, sort_by에 해당하는 값을 기준으로 오름차순 정렬 -> return
# ext, sort_by 값 - "code", "date","maximum", "remain"
# 1. ext - 값 찾기
# 2. val_ext보다 작은 데이터 뽑기
# 3. sort_by에 해당하는 값 기준 오름차순 정렬

def solution(data, ext, val_ext, sort_by):
    col = ["code","date","maximum","remain"]
    answer = []
    
    for i in range(len(data)):
        if data[i][col.index(ext)] < val_ext: 
            answer.append(data[i])
    
    
    
    answer.sort(key=lambda x : x[col.index(sort_by)])
    return answer
    