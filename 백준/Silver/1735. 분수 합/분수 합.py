import sys
input = sys.stdin.readline

def gcd(x,y):
    mod  = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y


A,B = map(int,input().split())
C,D = map(int,input().split())

top = B*C + A*D
bottom = B*D

g = gcd(top,bottom)
print(top // g, bottom // g)


