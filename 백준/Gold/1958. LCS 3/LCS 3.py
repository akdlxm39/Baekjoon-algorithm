import sys
input = sys.stdin.readline

def main():
    s1, s2, s3 = input().rstrip(), input().rstrip(), input().rstrip()
    dp = [[[0]*(len(s3)+1) for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i, c1 in enumerate(s1, 1):
        for j, c2 in enumerate(s2, 1):
            for k, c3 in enumerate(s3, 1):
                if c1 == c2 == c3:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    print(dp[-1][-1][-1])

if __name__ == "__main__":
    main()