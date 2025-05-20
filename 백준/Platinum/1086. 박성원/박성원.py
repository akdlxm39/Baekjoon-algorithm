import sys, math
input = sys.stdin.readline

def bottom_up(n, k, nums, tens):
    dp = [[0]*k for _ in range(1<<n)]
    dp[0][0] = 1
    for mask in range(1<<n):
        bit = 1
        for num, length in nums:
            if not mask & bit:
                for cur in range(k):
                    nxt = (cur*tens[length]+num)%k
                    dp[mask|bit][nxt] += dp[mask][cur]
            bit <<= 1
    return dp[-1][0]

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
    p = bottom_up(n, k, nums, tens)
    p_all = math.factorial(n)
    gcd = math.gcd(p, p_all)
    print(f"{p//gcd}/{p_all//gcd}")

if __name__ == "__main__":
    main()