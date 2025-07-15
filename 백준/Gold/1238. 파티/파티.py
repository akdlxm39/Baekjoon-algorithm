import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def xtoi(n, adj_list, x):
    heap = [(0, x)]
    dists = [INF] * (n + 1)
    dists[x] = 0
    while heap:
        cur_dist, cur = heappop(heap)
        if dists[cur] < cur_dist: continue
        for nxt, dist in adj_list[cur]:
            nxt_dist = cur_dist + dist
            if dists[nxt] <= nxt_dist: continue
            dists[nxt] = nxt_dist
            heappush(heap, (nxt_dist, nxt))
    return dists

def itox(n, adj_list, i, x):
    heap = [(0, i)]
    dists = [INF] * (n + 1)
    dists[i] = 0
    while heap:
        cur_dist, cur = heappop(heap)
        if dists[cur] < cur_dist: continue
        if cur == x: return dists[cur]
        for nxt, dist in adj_list[cur]:
            nxt_dist = cur_dist + dist
            if dists[nxt] <= nxt_dist: continue
            dists[nxt] = nxt_dist
            heappush(heap, (nxt_dist, nxt))
    return dists[x]

def main():
    n, m, x = map(int, input().split())
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        adj_list[a].append((b, t))
    dists = xtoi(n, adj_list, x)
    for i in range(1, n + 1):
        dists[i] += itox(n, adj_list, i, x)
    print(max(dists[1:]))

if __name__ == "__main__":
    main()