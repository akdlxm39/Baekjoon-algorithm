import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
INF = int(1e10)

def dist(A, B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1])

def dfs(n, w, case, dp, dp_trace, a, b):
    if dp[a][b] != -1:
        return dp[a][b]
    nxt = max(a, b)+1
    if nxt > w-1:
        return 0
    tmp1 = dfs(n, w, case, dp, dp_trace, a, nxt) + dist(case[nxt], case[b])
    tmp2 = dfs(n, w, case, dp, dp_trace, nxt, b) + dist(case[nxt], case[a])
    if tmp1 < tmp2:
        dp_trace[a][b] = 2
    else:
        dp_trace[a][b] = 1
    dp[a][b] = min(tmp1, tmp2)
    return dp[a][b]

def trace(w, dp_trace, a, b):
    nxt = max(a, b) + 1
    if nxt > w-1:
        return
    cur = dp_trace[a][b]
    print(cur, end='\n')
    if cur == 1:
        trace(w,dp_trace, nxt, b)
    else:
        trace(w, dp_trace, a, nxt)

def main():
    n, w = int(input()), int(input())
    case = [(1, 1), (n, n)] + [tuple(map(int, input().split())) for _ in range(w)]
    w += 2
    dp = [[-1]*w for _ in range(w)]
    dp_trace = [[0]*w for _ in range(w)]
    print(dfs(n, w, case, dp, dp_trace, 0, 1))
    trace(w, dp_trace, 0, 1)

if __name__ == "__main__":
    main()