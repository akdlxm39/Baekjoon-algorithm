import sys
sys.setrecursionlimit(30000)
input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def eat(n, bamboos, memo, x, y):
    if memo[x][y]:
        return memo[x][y]
    res = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n and bamboos[nx][ny] < bamboos[x][y]:
            res = max(res, eat(n, bamboos, memo, nx, ny))
    memo[x][y] = res+1
    return memo[x][y]

def main():
    n = int(input())
    bamboos = [list(map(int, input().split())) for _ in range(n)]
    memo = [[0]*n for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            ans = max(ans, eat(n, bamboos, memo, i, j))
    print(ans)

if __name__ == "__main__":
    main()