import sys
input = sys.stdin.readline

def main():
    n = int(input())
    p = list(map(int, input().split()))
    m = int(input())
    dp = [-1]*(m+1)
    for i in range(n-1, -1, -1):
        pi = p[i]
        for j in range(pi, m+1):
            dp[j] = max(dp[j], dp[j-pi]*10+i, i)
    print(dp[m])

if __name__ == "__main__":
    main()