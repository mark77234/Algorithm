r = int(input())
answer = 0

for i in range(r):
    word = input()
    tmp = []
    isGroup = False
    for w in word:
        if w in tmp and tmp[-1] != w:
            
            isGroup = True
        else:
            tmp.append(w)
            
    if not isGroup:
        answer += 1
    
        
            

print(answer)