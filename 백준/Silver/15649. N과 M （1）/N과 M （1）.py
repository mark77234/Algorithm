from itertools import permutations

number, size = map(int,input().split())

numbers= []
for i in range(1,number+1):
    numbers.append(i)

answer = list(permutations(numbers,size))

for a in answer:
    print(*a)