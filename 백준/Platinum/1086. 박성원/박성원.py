import sys, math
input = sys.stdin.readline

def dfs(n, k, nums, tens, dp, cur, bitmask, cnt):
    if cnt == n:
        return cur == 0
    if dp[bitmask][cur] != -1:
        return dp[bitmask][cur]
    dp[bitmask][cur] = 0
    mask = 1
    for i in range(n):
        if not bitmask & mask:
            nxt = (cur * tens[nums[i][1]] + nums[i][0]) % k
            dp[bitmask][cur] += dfs(n, k, nums, tens, dp, nxt, bitmask|mask, cnt + 1)
        mask <<= 1
    return dp[bitmask][cur]

def main():
    n = int(input())
    nums = [input().rstrip() for _ in range(n)]
    k = int(input())
    for i in range(n):
        length = len(nums[i])
        tmp = 0
        for c in nums[i]:
            tmp = tmp*10+int(c)
            tmp %= k
        nums[i] = (tmp, length)
    tens = [1] + [0] * 50
    for i in range(1, 51):
        tens[i] = tens[i-1] * 10 % k
    dp = [[-1]*100 for _ in range(1<<n)]
    p = dfs(n, k, nums, tens, dp, 0, 0, 0)
    Max = math.factorial(n)
    gcd = math.gcd(p, Max)
    print(f"{p//gcd}/{Max//gcd}")

if __name__ == "__main__":
    main()