import sys

input = sys.stdin.readline


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    MAX_GAP = sum(nums) // 2
    dp = [[-1] * (MAX_GAP + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i, h in enumerate(nums, 1):
        for gap in range(MAX_GAP + 1):
            cur = dp[i - 1][gap]
            if dp[i - 1][gap] == -1: continue
            dp[i][gap] = max(dp[i][gap], cur)
            if gap + h <= MAX_GAP:
                dp[i][gap + h] = max(dp[i][gap + h], cur + h)
            if abs(gap - h) <= MAX_GAP:
                dp[i][abs(gap - h)] = max(dp[i][abs(gap - h)], cur - gap + h, cur)
    print(dp[n][0] if dp[n][0] > 0 else -1)


if __name__ == "__main__":
    main()
