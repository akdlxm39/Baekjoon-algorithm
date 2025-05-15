import sys
input = sys.stdin.readline

def main():
    n = int(input())
    if n % 2 == 1:
        print(0)
        return
    n //= 2
    dp = [1] + [0] * n
    for i in range(1, n+1):
        for j in range(0, i):
            dp[i] += dp[j]*2
        dp[i] += dp[i-1]
    print(dp[n])

if __name__ == "__main__":
    main()