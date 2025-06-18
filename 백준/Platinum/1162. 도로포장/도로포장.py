import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def main():
    n, m, k = map(int, input().split())
    roads = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, cost = map(int, input().split())
        roads[u].append((v, cost))
        roads[v].append((u, cost))
    costs = [[INF]*(k+1) for _ in range(n+1)]
    visited = [k+1]*(n+1)
    heap = [(0, 0, 1)] # total_cost, used, node
    while heap:
        cost, used, cur = heappop(heap)
        if cur == n: print(cost) ; break
        if used >= visited[cur]: continue
        visited[cur] = used
        costs[cur][used] = cost
        for nxt, nxt_cost in roads[cur]:
            if visited[nxt] > used:
                heappush(heap, (cost+nxt_cost, used, nxt))
            if visited[nxt] > used+1:
                heappush(heap, (cost, used+1, nxt))
    else:
        print(-1)

if __name__ == "__main__":
    main()