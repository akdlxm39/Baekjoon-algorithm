import sys

input = sys.stdin.readline
INF = int(1e9)

def dynamic(n, w, areas, last_used):
    if areas[0][1] + areas[-1][1] > w and (last_used==1 or last_used==3):
        return INF
    elif areas[0][0] + areas[-1][0] > w and (last_used==2 or last_used==3):
        return INF
    dp = [[INF for _ in range(5)] for _ in range(n)]
    # (s,s), (s,l), (l,s), (l,l), (d,u)
    dp[0][last_used] = 2
    if last_used==0 and areas[0][0] + areas[0][1] <= w:
        dp[0][4] = 1
    for i in range(1, n):
        dp[i][0] = min(dp[i-1]) + 2
        if areas[i][1] + areas[i-1][1] <= w:
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + 1
            if areas[i][0] + areas[i-1][0] <= w:
                dp[i][3] = dp[i-1][0]
        if areas[i][0] + areas[i-1][0] <= w:
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + 1
        if areas[i][0] + areas[i][1] <= w:
            dp[i][4] = min(dp[i-1]) + 1
    if last_used==0:
        return min(dp[-1])
    elif last_used==1:
        return min(dp[-1][0], dp[-1][2]) - 1
    elif last_used==2:
        return min(dp[-1][0], dp[-1][1]) - 1
    elif last_used==3:
        return min(dp[-2])



def main():
    t = int(input())
    for _ in range(t):
        n, w = map(int, input().split())
        areas = list(zip(map(int, input().split()), map(int, input().split())))
        if n == 1:
            print(1 if sum(areas[0]) <= w else 2)
            continue
        ans = INF
        for i in range(4):
            ans = min(ans, dynamic(n, w, areas, i))
        print(ans)


if __name__ == "__main__":
    main()
