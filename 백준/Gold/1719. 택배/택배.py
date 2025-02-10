import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(n, adj, x):
    costs = [INF] * (n+1)
    result = ['-'] * (n+1)
    costs[x] = 0
    heap = [(0, x)]
    while heap:
        cur_cost, cur = heappop(heap)
        if cur_cost > costs[cur]:
            continue
        for c, i in adj[cur]:
            nxt_cost = cur_cost + c
            if nxt_cost < costs[i]:
                costs[i] = nxt_cost
                result[i] = result[cur] if cur!=x else i
                heappush(heap, (nxt_cost, i))
    return result[1:]

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, cost = map(int, input().split())
        adj[u].append((cost, v))
        adj[v].append((cost, u))
    for i in range(1, n+1):
        print(' '.join(map(str, dijkstra(n, adj, i))))

if __name__ == "__main__":
    main()