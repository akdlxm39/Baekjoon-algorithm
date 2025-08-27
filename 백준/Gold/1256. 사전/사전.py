import sys

input = sys.stdin.readline


def combi(combi_dp, n, k):
    if combi_dp[n][k] == -1:
        if n < k:
            combi_dp[n][k] = 0
        elif k == 0 or n == k:
            combi_dp[n][k] = 1
        else:
            combi_dp[n][k] = (combi(combi_dp, n - 1, k) +
                              combi(combi_dp, n - 1, k - 1))
    return combi_dp[n][k]

def solve(combi_dp, n, m, k, word):
    if n == 0:
        return word + 'z' * m
    elif m == 0:
        return word + 'a' * n
    if k <= combi(combi_dp, n + m - 1, n - 1):
        return solve(combi_dp, n - 1, m, k, word + 'a')
    else:
        k -= combi(combi_dp, n + m - 1, n - 1)
        return solve(combi_dp, n, m - 1, k, word + 'z')


def main():
    n, m, k = map(int, input().split())
    combi_dp = [[-1] * (n + m + 1) for _ in range(n + m + 1)]
    if combi(combi_dp, n + m, n) < k:
        print(-1)
        return
    print(solve(combi_dp, n, m, k, ''))


if __name__ == "__main__":
    main()
