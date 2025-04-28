import sys
input = sys.stdin.readline

MOD = 1000000007

def main():
    N = int(input())
    _, answer = func(N)
    answer = answer * 2 * power(power(2, N), MOD-2) % MOD
    print(answer)

def power(X, e):
    if e == 1:
        return X % MOD
    return (power(X, e//2) ** 2) * X % MOD if e%2 else power(X, e//2) ** 2 % MOD

def func(e): #(a +- b(sqrt5))^e
    if e == 1:
        return 1, 1
    a, b = func(e//2)
    if e%2:
        return (a**2 + 5 * (b**2) + 10 * a * b) % MOD, (a**2 + 5 * (b**2) + 2 * a * b) % MOD
    else:
        return (a**2 + 5 * (b**2)) % MOD, (2 * a * b) % MOD

main()