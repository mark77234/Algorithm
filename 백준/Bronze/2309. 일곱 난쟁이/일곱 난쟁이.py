""" solve.py for 2309 """

import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

# 아홉 난쟁이 중 두 명의 가짜 난쟁이를 찾아야 함
# 일곱 난쟁이 키의 합은 100
# 아홉 난쟁이 총합 - 100 = 나머지 가짜 난쟁이들의 합
# 이중 포문으로 모든 경우의 수 종합 target과 같은경우 return

def solve(heights:list[int]):
    total = sum(heights)
    target = total - 100
    
    n = len(heights)
    
    for i in range(n):
        for j in range(i+ 1,n):
            if heights[i] + heights[j] == target:
                return sorted(h for h in heights if h not in (heights[i],heights[j]))
    
    return []

def main() -> None:
    heights = [int(sys_input()) for _ in range(9) ]
    
    answer : list[int] = solve(heights)
    
    print(*answer,sep="\n")
    

if __name__ == "__main__":
    main()