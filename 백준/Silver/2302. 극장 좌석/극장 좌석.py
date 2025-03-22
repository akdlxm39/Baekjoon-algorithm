import sys
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    vip = [0] + [int(input()) for _ in range(m)] + [n+1]
    gap = [vip[i]-vip[i-1]-1 for i in range(1, m+2)]
    dp = [1, 1]
    for i in range(2, max(gap)+1):
        dp.append(dp[i-2] + dp[i-1])
    ans = 1
    for x in gap:
        ans *= dp[x]
    print(ans)

if __name__ == "__main__":
    main()