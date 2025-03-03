import sys
input = sys.stdin.readline

def main():
    A, B = input().rstrip(), input().rstrip()
    dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
    for i, a in enumerate(A,1):
        for j, b in enumerate(B,1):
            if a == b:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    print(dp[-1][-1])
    
main()