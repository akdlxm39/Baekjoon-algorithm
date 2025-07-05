import sys
input = sys.stdin.readline
MOD = 1_000_000_007

def get_factorial(n):
    res = [0] * (n + 1)
    res[0] = res[1] = 1
    for i in range(2, n+1):
        res[i] = res[i-1] * i % MOD
    return res

def power(x, n):
    if n == 0:
        return 1
    res = 1
    while n:
        if n&1:
            res = res * x % MOD
        x = x * x % MOD
        n = n>>1
    return res


def main():
    m = int(input())
    factorial = get_factorial(4_000_000)
    ans = [0]*m
    for i in range(m):
        n, k = map(int, input().split())
        tmp = factorial[k] * factorial[n-k] % MOD
        ans[i] = power(tmp, MOD-2) * factorial[n] % MOD
    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    main()