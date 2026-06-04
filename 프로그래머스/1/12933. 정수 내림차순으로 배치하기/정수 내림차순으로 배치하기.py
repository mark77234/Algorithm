def solution(n):
    li = []
    n = str(n)
    answer = ""
    for number in n:
        li.append(int(number))
    li.sort(reverse = True)
    
    for number in li:
        answer += str(number)
    print(answer)
    return int(answer)