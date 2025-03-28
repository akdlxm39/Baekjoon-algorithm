import sys
input = sys.stdin.readline

def main():
    n = int(input())
    dp = [0, 0]
    for i in range(n-1):
        if i%2:
            dp.append((dp[-1]*2-1)%1_000_000_007)
        else:
            dp.append((dp[-1]*2+1)%1_000_000_007)
    print(dp[n])

if __name__ == "__main__":
    main()