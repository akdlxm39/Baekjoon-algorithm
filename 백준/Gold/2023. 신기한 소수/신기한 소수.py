import sys

input = sys.stdin.readline


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def dfs(n, cur, cnt):
    if cnt == n:
        print(cur)
        return
    for i in range(1, 10):
        nxt = cur * 10 + i
        if is_prime(nxt):
            dfs(n, nxt, cnt + 1)


def main():
    n = int(input())
    dfs(n, 0, 0)


if __name__ == "__main__":
    main()
