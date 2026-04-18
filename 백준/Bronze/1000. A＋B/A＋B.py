""" solve.py for 1000번. A+B"""

import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()

def solve(a: int, b: int) -> int:
    return a + b


def main() -> None:
    a,b = map(int,sys_input().split())
    
    answer: int = solve(a,b)
    print(answer)
    
if __name__ == "__main__":
    main()