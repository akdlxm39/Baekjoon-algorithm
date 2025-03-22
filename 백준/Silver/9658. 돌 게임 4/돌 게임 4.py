import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [True, False, True, False]
    for i in range(4, n+1):
        dp.append(not(dp[i-1] and dp[i-3] and dp[i-4]))
    print("SK" if dp[n] else "CY")

if __name__ == "__main__":
    main()