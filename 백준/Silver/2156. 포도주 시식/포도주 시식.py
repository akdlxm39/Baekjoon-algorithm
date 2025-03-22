import sys
input = sys.stdin.readline

def main():
    N = int(input())
    stairs = [int(input()) for _ in range(N)]
    dp = [[0]*2 for _ in range(N+1)]
    for i, s in enumerate(stairs, 1):
        dp[i][0] = s + (max(dp[i-3][0], dp[i-3][1], dp[i-2][0], dp[i-2][1]) if i>=3 else max(dp[i-2][0], dp[i-2][1]) if i >= 2 else 0)
        dp[i][1] = s + dp[i-1][0]
    print(max(dp[-1] + dp[-2]))

main()