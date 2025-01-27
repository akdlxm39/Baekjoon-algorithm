import sys
from functools import reduce
from math import gcd
input = sys.stdin.readline

def solve(n, visited, ratio, x=14, y=14):
    if n == 0:
        return 1
    ans = 0
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited[x][y] = True
    for i in range(4):
        dx, dy = x+dir[i][0], y + dir[i][1]
        if visited[dx][dy]:
            continue
        ans += ratio[i] * solve(n-1, visited, ratio, dx, dy)
    visited[x][y] = False
    return ans

def main():
    n, *ratio = map(int, input().split())
    x = reduce(gcd, ratio)
    ratio = list(map(lambda a: a//x, ratio))
    visited = [[False]*29 for _ in range(29)]
    print(solve(n, visited, ratio)/(sum(ratio))**n)

if __name__ == "__main__":
    main()