import sys
input = sys.stdin.readline

def main():
    o = input().rstrip()
    n = input().rstrip()
    dp = [(0, True)] + [(0, False) for _ in range(len(n))]
    for i, x in enumerate(o, 1):
        tmp = [(0, False)]
        mindp = 1000
        for j, y in enumerate(n, 1):
            if dp[j-1][1]:
                mindp = min(mindp, dp[j-1][0])
            if x == y:
                if dp[j-1][1]:
                    tmp.append((dp[j-1][0], True))
                elif mindp != 1000:
                    tmp.append((mindp+1, True))
                else:
                    tmp.append((0, False))
            else:
                tmp.append((0, False))
        dp = tmp
    ans = [x + (i!=len(n)) for i, (x, b) in enumerate(dp) if b]
    print(min(ans) if ans else -1)

if __name__ == "__main__":
    main()