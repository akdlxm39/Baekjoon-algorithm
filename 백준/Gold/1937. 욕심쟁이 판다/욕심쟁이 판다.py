import sys
sys.setrecursionlimit(30000)
input = sys.stdin.readline

def eat(n, bamboos, memo, x, y):
    if memo[x][y]:
        return memo[x][y]
    res = [0]
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        nx, ny = x+dx, y+dy
        if bamboos[nx][ny] > bamboos[x][y]:
            res.append(eat(n, bamboos, memo, nx, ny))
    memo[x][y] = max(res)+1
    return memo[x][y]

def main():
    n = int(input())
    bamboos = ([[0]*(n+2)]+
               [[0]+list(map(int, input().split()))+[0] for _ in range(n)]+
               [[0]*(n+2)])
    memo = [[0]*(n+2) for _ in range(n+2)]
    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            ans = max(ans, eat(n, bamboos, memo, i, j))
    print(ans)

if __name__ == "__main__":
    main()