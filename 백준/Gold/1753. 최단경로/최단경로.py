import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline
INF = 3000001

def dijkstra(dp, adj_list, k):
    heap = [(0, k)]
    while heap:
        cost, u = heappop(heap)
        if cost > dp[u]:
            continue
        for v, w in adj_list[u]:
            if dp[v] > dp[u]+w:
                dp[v] = dp[u]+w
                heappush(heap, (dp[v], v))

def main():
    n, m = map(int, input().split())
    k = int(input())
    dp = [INF]*(n+1)
    dp[k] = 0
    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj_list[u].append((v, w))
    dijkstra(dp, adj_list, k)
    for d in dp[1:]:
        if d == INF:
            print("INF")
        else:
            print(d)

if __name__ == "__main__":
    main()