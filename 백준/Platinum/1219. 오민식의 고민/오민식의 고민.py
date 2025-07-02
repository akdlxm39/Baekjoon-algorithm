import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(n, edges, profits, dest):
    cycle_list = []
    for _ in range(n-1):
        for cur in range(n):
            for nxt, earned in edges[cur].items():
                nxt_profit = profits[cur] + earned
                if profits[cur] != -INF and profits[nxt] < nxt_profit:
                    profits[nxt] = nxt_profit
    for cur in range(n):
        for nxt, earned in edges[cur].items():
            nxt_profit = profits[cur] + earned
            if profits[cur] != -INF and profits[nxt] < nxt_profit:
                profits[nxt] = nxt_profit
                cycle_list.append(nxt)
    return cycle_list

def check(n, edges, cycle_list, dest):
    visited = [False] * n
    queue = deque(cycle_list)
    for cur in cycle_list:
        visited[cur] = True
    while queue:
        cur = queue.popleft()
        for nxt in edges[cur].keys():
            if visited[nxt]: continue
            visited[nxt] = True
            queue.append(nxt)
    return visited[dest]

def main():
    n, s, d, m = map(int, input().split())
    edges = [{} for _ in range(n)]
    for _ in range(m):
        u, v, cost = map(int, input().split())
        if v in edges[u]:
            edges[u][v] = max(edges[u][v], -cost)
        else:
            edges[u][v] = -cost
    revenues = list(map(int, input().split()))
    for cur in range(n):
        for nxt in edges[cur].keys():
            edges[cur][nxt] += revenues[nxt]
    profits = [-INF] * n
    profits[s] = revenues[s]
    cycle_list = bellman_ford(n, edges, profits, d)
    if profits[d] == -INF:
        print("gg")
    elif cycle_list and check(n, edges, cycle_list, d):
        print("Gee")
    else:
        print(profits[d])

if __name__ == "__main__":
    main()