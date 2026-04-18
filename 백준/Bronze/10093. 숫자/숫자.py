"""solve.py for 10093"""

import sys

def sys_input():
    return sys.stdin.readline().rstrip()

# A와 B의 대소관계가 정해지지 않았음 min()/max() 처리
def solve(a:int,b:int)-> list[int]:
    lo,hi = min(a,b), max(a,b)

    between = list(range(lo+1,hi))
    
    return len(between), between

# 개수는 max - min - 1
def main() -> None:
    a,b = map(int,sys_input().split())
    answer: tuple[int,list[int]] = solve(a,b)
    
    print(answer[0])
    print(*answer[1])

if __name__ == "__main__":
    main()