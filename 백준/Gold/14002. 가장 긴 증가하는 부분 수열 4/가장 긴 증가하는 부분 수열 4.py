import sys
from bisect import bisect_left

input = sys.stdin.readline


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    dp = []
    dpi = []
    prev = [-1] * n
    for i, num in enumerate(nums):
        if not dpi:
            dpi.append(i)
            dp.append(num)
        elif nums[i] > nums[dpi[-1]]:
            prev[i] = dpi[-1]
            dpi.append(i)
            dp.append(num)
        else:
            idx = bisect_left(dp, num)
            prev[i] = dpi[idx-1] if idx > 0 else -1
            dpi[idx] = i
            dp[idx] = num
    tmp = dpi[-1]
    res = []
    while tmp != -1:
        res.append(nums[tmp])
        tmp = prev[tmp]
    print(len(dp))
    print(*reversed(res))


if __name__ == "__main__":
    main()
