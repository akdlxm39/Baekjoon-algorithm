import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def bellman_ford(n, revenues, profits):
    for _ in range(n-1):
        for cur, nxt, earned in revenues:
            nxt_profit = profits[cur] + earned
            if profits[cur] != -INF and profits[nxt] < nxt_profit:
                profits[nxt] = nxt_profit
    cycle_list = []
    for cur, nxt, earned in revenues:
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
        if cur == dest: return True
        for nxt in edges[cur]:
            if visited[nxt]: continue
            visited[nxt] = True
            queue.append(nxt)
    return False

def main():
    n, s, d, m = map(int, input().split())
    revenues = [list(map(int, input().split())) for _ in range(m)]
    moneys = list(map(int, input().split()))
    edges = [[] for _ in range(n)]
    for i in range(m):
        revenues[i][2] = moneys[revenues[i][1]] - revenues[i][2]
        edges[revenues[i][0]].append(revenues[i][1])
    profits = [-INF] * n
    profits[s] = moneys[s]
    cycle_list = bellman_ford(n, revenues, profits)
    if profits[d] == -INF:
        print("gg")
    elif cycle_list and check(n, edges, cycle_list, d):
        print("Gee")
    else:
        print(profits[d])

if __name__ == "__main__":
    main()