import sys

input = sys.stdin.readline
INF = int(1e9)
dx, dy = [1, 0, 0], [0, 1, -1]

def main():
    n, m = map(int, input().split())
    mars = [list(map(int, input().split())) for _ in range(n)] + [[0]*m]
    dp = [[[-INF]*3 for _ in range(m)] for _ in range(n+1)]
    dp[0][0][0] = dp[0][0][1] = mars[0][0]
    dp[1][0][0] = mars[0][0] + mars[1][0]
    for i in range(1, m):
        dp[0][i][1] = dp[0][i-1][1] + mars[0][i]
        dp[1][i][0] = dp[0][i][1] + mars[1][i]
    for i in range(1, n):
        for j in range(m-1, 0, -1):
            dp[i][j-1][2] = max(dp[i][j][0], dp[i][j][2]) + mars[i][j-1]
        dp[i+1][0][0] = max(dp[i][0]) + mars[i+1][0]
        for j in range(m-1):
            dp[i][j+1][1] = max(dp[i][j][0], dp[i][j][1]) + mars[i][j+1]
            dp[i+1][j+1][0] = max(dp[i][j+1]) + mars[i+1][j+1]
    print(dp[-1][-1][0])




if __name__ == "__main__":
    main()
