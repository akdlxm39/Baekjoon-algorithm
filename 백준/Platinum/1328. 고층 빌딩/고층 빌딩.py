import sys
input = sys.stdin.readline
MOD = 1_000_000_007

def main():
    n, l, r = map(int, input().split())
    dp = [[[0]*(r+1) for _ in range(l+1)] for _ in range(n+1)]
    dp[n][1][1] = 1
    for k in range(n-1, 0, -1):
        for i in range(l, 0, -1):
            for j in range(r, 0, -1):
                dp[k][i][j] = (dp[k+1][i-1][j] + dp[k+1][i][j-1] + dp[k+1][i][j] * (n-k-1)) % MOD
    print(dp[1][l][r])

if __name__ == "__main__":
    main()