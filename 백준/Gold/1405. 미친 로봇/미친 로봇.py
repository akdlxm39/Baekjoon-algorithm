import sys
from functools import reduce
from math import gcd
input = sys.stdin.readline

def solve(n, visited, ratio, x=0, y=0):
    if n == 0:
        return 1
    ans = 0
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited.add((x, y))
    for i in range(4):
        dx, dy = x+dir[i][0], y + dir[i][1]
        if (dx, dy) in visited:
            continue
        ans += ratio[i] * solve(n-1, visited, ratio, dx, dy)
    visited.remove((x, y))
    return ans

def main():
    n, *ratio = map(int, input().split())
    x = reduce(gcd, ratio)
    ratio = list(map(lambda a: a//x, ratio))
    visited = set()
    print(solve(n, visited, ratio, x)/(sum(ratio))**n)

if __name__ == "__main__":
    main()