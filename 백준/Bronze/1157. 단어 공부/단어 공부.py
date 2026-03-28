a = input().upper()

words = list(set(a))
answer = []

for w in words:
    answer.append(a.count(w))

if answer.count(max(answer)) >= 2:
    print('?')
else:
    print(words[answer.index(max(answer))])
    

    
        