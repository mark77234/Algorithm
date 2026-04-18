"""solve.py for 2587"""

import sys

def sys_input()->str:
    return sys.stdin.readline().strip()

def solve(li : list[int])->tuple[int,int]:
    return sum(li) // len(li), sorted(li)[len(li) // 2]
    

def main():
    li = [int(sys_input()) for _ in range(5)]
    answer:tuple[int,int] = solve(li)
    
    print(*answer,sep="\n")

if __name__ == "__main__":
    main()
    