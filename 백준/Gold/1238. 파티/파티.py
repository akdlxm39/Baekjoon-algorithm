import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def bfs(n, adj_list, x):
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

def main():
    n, m, x = map(int, input().split())
    adj_list1 = [[] for _ in range(n + 1)]
    adj_list2 = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, t = map(int, input().split())
        adj_list1[a].append((b, t))
        adj_list2[b].append((a, t))
    dists1 = bfs(n, adj_list1, x)
    dists2 = bfs(n, adj_list2, x)
    print(max(dists1[i] + dists2[i] for i in range(1, n + 1)))

if __name__ == "__main__":
    main()