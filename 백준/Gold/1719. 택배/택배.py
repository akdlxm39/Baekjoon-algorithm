import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def main():
    n, m = map(int, input().split())
    costs = [[INF if i!=j else 0 for j in range(n+1)] for i in range(n+1)]
    ans = [['-']*(n+1) for _ in range(n+1)]
    heap = []
    for _ in range(m):
        u, v, cost = map(int, input().split())
        costs[u][v] = costs[v][u] = cost
        heappush(heap, (cost, u, v, 0))
        heappush(heap, (cost, v, u, 0))
    x = n*(n-1)
    while x and heap:
        cur_cost, s, e, nxt = heappop(heap)
        if ans[s][e] != '-':
            continue
        ans[s][e] = nxt if nxt else e
        for i in range(1, n+1):
            if ans[i][e] != '-' or i == e or costs[i][s]==INF:
                continue
            heappush(heap, (cur_cost + costs[i][s], i, e, s))
        x-=1
    for line in ans[1:]:
        print(' '.join(map(str, line[1:])))


if __name__ == "__main__":
    main()