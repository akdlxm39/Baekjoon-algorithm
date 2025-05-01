import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        stickers = [list(map(int, input().split())) for _ in range(2)]
        dp = [[stickers[0][j], stickers[1][j], 0] for j in range(n)]
        for i in range(1, n):
            dp[i][0] += max(dp[i-1][1], dp[i-1][2])
            dp[i][1] += max(dp[i-1][0], dp[i-1][2])
            dp[i][2] += max(dp[i-1][0], dp[i-1][1])
        print(max(dp[-1]))

if __name__ == "__main__":
    main()