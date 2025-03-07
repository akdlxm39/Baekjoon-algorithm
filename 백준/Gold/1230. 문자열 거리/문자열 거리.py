import sys
input = sys.stdin.readline

def main():
    o = input().rstrip()
    n = input().rstrip()
    dp = [1] + [0]*len(n)
    for x in o:
        tmp = [0]
        mindp = 1000
        for i, y in enumerate(n, 1):
            if dp[i-1]:
                mindp = min(mindp, dp[i-1])
            if x == y:
                if dp[i-1]:
                    tmp.append(dp[i-1])
                elif mindp != 1000:
                    tmp.append(mindp+1)
                else:
                    tmp.append(0)
            else:
                tmp.append(0)
        dp = tmp
    ans = [x for x in dp[:-1] if x]
    if dp[-1]:
        ans.append(dp[-1] - 1)
    print(min(ans) if ans else -1)

if __name__ == "__main__":
    main()