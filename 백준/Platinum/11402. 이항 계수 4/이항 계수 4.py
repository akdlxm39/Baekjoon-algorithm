import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def binomial_coefficient(bc, n, m):
    if bc[n][m] != -1:
        return bc[n][m]
    if n < m:
        bc[n][m] = 0
    elif m == 0:
        bc[n][m] = 1
    else:
        bc[n][m] = (binomial_coefficient(bc, n - 1, m - 1) +
                    binomial_coefficient(bc, n - 1, m))
    return bc[n][m]


def main():
    n, k, m = map(int, input().split())
    bc = [[-1] * m for _ in range(m)]
    ans = 1
    while n and ans:
        ans = ans * binomial_coefficient(bc, n % m, k % m) % m
        n //= m
        k //= m
    print(ans)


if __name__ == "__main__":
    main()
