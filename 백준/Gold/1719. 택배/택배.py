import sys
input = sys.stdin.readline
INF = int(1e9)

def main():
    n, m = map(int, input().split())
    costs = [[INF if i!=j else 0 for j in range(n+1)] for i in range(n+1)]
    ans = [['-']*(n+1) for _ in range(n+1)]
    for _ in range(m):
        u, v, cost = map(int, input().split())
        costs[u][v] = costs[v][u] = cost
        ans[u][v] = v
        ans[v][u] = u
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                nxt_cost = costs[i][k] + costs[k][j]
                if nxt_cost < costs[i][j]:
                    costs[i][j] = nxt_cost
                    ans[i][j] = ans[i][k]
    for x in ans[1:]:
        print(' '.join(map(str, x[1:])))

if __name__ == "__main__":
    main()