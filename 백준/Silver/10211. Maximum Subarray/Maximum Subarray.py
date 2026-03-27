r = int(input())

for i in range(r):
    n = int(input())
    arr = list(map(int,input().split()))
    
    tot = arr[0]
    answer = arr[0]
    for a in arr[1:]:
        tot = max(a, tot + a)
        answer = max(tot,answer)
        if tot < 0:
            tot = 0
    
    print(answer)