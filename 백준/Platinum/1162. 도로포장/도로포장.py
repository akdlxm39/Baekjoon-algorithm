import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e10)

def main():
    n, m, k = map(int, input().split())
    roads = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, cost = map(int, input().split())
        roads[u].append((v, cost))
        roads[v].append((u, cost))
    dists = [[INF]*(n+1) for _ in range(k+1)]
    heap = [(0, k, 1)] # total_cost, used, node
    while heap:
        dist, used, cur = heappop(heap)
        if dist > dists[used][cur]: continue
        if cur == n: print(dist) ; break
        for nxt, nxt_cost in roads[cur]:
            nxt_dist = dist + nxt_cost
            if dists[used][nxt] > nxt_dist:
                dists[used][nxt] = nxt_dist
                heappush(heap, (nxt_dist, used, nxt))
            if used > 0 and dists[used-1][nxt] > dist:
                dists[used-1][nxt] = dist
                heappush(heap, (dist, used-1, nxt))

if __name__ == "__main__":
    main()