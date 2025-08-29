import sys

input = sys.stdin.readline

def get_primes(n):
    primes = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i + i::i] = [False] * (n // i - 1)
    return [i for i in range(2, n + 1) if primes[i]]

def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    primes = get_primes(n)
    size = len(primes)
    s, e = 0, 1
    cur = primes[s]
    ans = 0
    while s < size:
        if cur == n:
            ans += 1
        if cur < n and e < size:
            cur += primes[e]
            e += 1
        else:
            cur -= primes[s]
            s += 1
    print(ans)


if __name__ == "__main__":
    main()
