import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    nums = [input().rstrip() for _ in range(n)]
    dp = [[0] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if nums[i][j] == '0':
                continue
            size = min(dp[i][j - 1], dp[i - 1][j])
            for k in range(size, 0, -1):
                if nums[i - k][j - k] == '1':
                    dp[i][j] = k + 1
                    break
            else:
                dp[i][j] = 1
            ans = max(ans, dp[i][j])
    print(ans * ans)


if __name__ == "__main__":
    main()
