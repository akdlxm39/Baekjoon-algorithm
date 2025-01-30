import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline
INF = 3000001

def dijkstra(dp, adj_list, k):
    heap = [(0, k)]
    while heap:
        _, u = heappop(heap)
        if u not in adj_list:
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
    not_checked = set(range(1, n+1))
    not_checked.remove(k)
    adj_list = dict()
    for _ in range(m):
        u, v, w = map(int, input().split())
        if u in adj_list:
            adj_list[u].append((v, w))
        else:
            adj_list[u] = [(v, w)]
    dijkstra(dp, adj_list, k)
    for d in dp[1:]:
        if d == INF:
            print("INF")
        else:
            print(d)

if __name__ == "__main__":
    main()