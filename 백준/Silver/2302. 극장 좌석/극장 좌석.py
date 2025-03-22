import sys
input = sys.stdin.readline

def main():
    N = int(input())
    M = int(input())
    vip = [0] + [int(input()) for _ in range(M)] + [N+1]
    gap = [vip[i] - vip[i-1] - 1 for i in range(1, len(vip))]
    dp = [1, 1]
    for i in range(2, max(gap)+1):
        dp.append(dp[i-2] + dp[i-1])
    answer = 1
    for g in gap:
        answer *= dp[g]
    print(answer)

if __name__ == "__main__":
    main()