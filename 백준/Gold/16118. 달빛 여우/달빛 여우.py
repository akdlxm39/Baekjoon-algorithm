import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline
INF = 1e9

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    fox = [INF] * (n + 1)
    fox_heap = [(0, 1)]
    while fox_heap:
        cur_dist, cur = heappop(fox_heap)
        if fox[cur] < cur_dist:
            continue
        fox[cur] = cur_dist
        for x, d in graph[cur]:
            nxt_dist = cur_dist + d
            if nxt_dist < fox[x]:
                fox[x] = nxt_dist
                heappush(fox_heap, (nxt_dist, x))
    wolf = [[INF, INF] for _ in range(n+1)]
    wolf[1][0] = 0
    wolf_heap = [(0, 1, 1)]
    while wolf_heap:
        cur_dist, cur, fast = heappop(wolf_heap)
        slow = 1 - fast
        if wolf[cur][slow] < cur_dist:
            continue
        speed = 0.5 if fast else 2
        for x, d in graph[cur]:
            nxt_dist = cur_dist + d * speed
            if nxt_dist < wolf[x][fast]:
                wolf[x][fast] = nxt_dist
                heappush(wolf_heap, (nxt_dist, x, slow))
    ans = 0
    for i in range(2, n+1):
        ans += fox[i] < min(wolf[i])
    print(ans)

if __name__ == "__main__":
    main()