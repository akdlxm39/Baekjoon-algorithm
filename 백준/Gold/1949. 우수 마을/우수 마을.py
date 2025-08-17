import sys

sys.setrecursionlimit(10005)
input = sys.stdin.readline
INF = int(1e9)


def dfs(n, people, roads, visited, dp, cur):
    visited[cur] = True
    children = []
    for nxt in roads[cur]:
        if visited[nxt]: continue
        children.append(nxt)
        dfs(n, people, roads, visited, dp, nxt)
    flag = False
    gap = -INF
    for child in children:
        dp[cur][0] += dp[child][1]
        dp[cur][2] += max(dp[child][0], dp[child][1])
        if dp[child][1] <= dp[child][2]:
            flag = True
            dp[cur][1] += dp[child][2]
        else:
            dp[cur][1] += dp[child][1]
            gap = max(gap, dp[child][2] - dp[child][1])
    if not flag:
        dp[cur][1] += gap


def main():
    n = int(input())
    people = list(map(int, input().split()))
    roads = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(lambda x: int(x) - 1, input().split())
        roads[u].append(v)
        roads[v].append(u)
    visited = [False] * n
    dp = [[0, 0, people[i]] for i in range(n)]
    dfs(n, people, roads, visited, dp, 0)
    print(max(dp[0]))


if __name__ == "__main__":
    main()
