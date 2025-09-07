import sys

input = sys.stdin.readline


def get_primes(n):
    primes = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i + i::i] = [False] * (n // i - 1)
    return primes


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def dfs(n, primes, cur, cnt):
    if cnt == n:
        print(cur)
        return
    elif cnt >= 5:
        for i in range(1, 10):
            nxt = cur * 10 + i
            if is_prime(nxt):
                dfs(n, primes, nxt, cnt + 1)
        return
    else:
        for i in range(1, 10):
            nxt = cur * 10 + i
            if primes[nxt]:
                dfs(n, primes, nxt, cnt + 1)


def main():
    n = int(input())
    primes = get_primes(99999)
    dfs(n, primes, 0, 0)


if __name__ == "__main__":
    main()
