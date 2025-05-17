import sys
from heapq import heappush, heappop
from collections import deque
input = sys.stdin.readline

def shortest_path(n, s, roads):
    heap = [(0, s, s)]
    prevs = [[-1] for _ in range(n)]
    prevs[s] = [0]
    while heap:
        dist, cur, prev = heappop(heap)
        if dist != prevs[cur][0]: continue
        prevs[cur].append(prev)
        for nxt in range(n):
            if roads[cur][nxt] == -1: continue
            nxt_dist = dist + roads[cur][nxt]
            if prevs[nxt][0] == -1 or nxt_dist < prevs[nxt][0]:
                prevs[nxt] = [nxt_dist, cur]
                heappush(heap, (nxt_dist, nxt, cur))
            elif nxt_dist == prevs[nxt][0]:
                prevs[nxt].append(cur)
    return prevs

def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0: break
        s, d = map(int, input().split())
        roads = [[-1] * n for _ in range(n)]
        for _ in range(m):
            u, v, p = map(int, input().split())
            roads[u][v] = p
        prevs = shortest_path(n, s, roads)
        queue = deque([d])
        deleted = [False] * n
        deleted[s] = True
        while queue:
            cur = queue.popleft()
            for prev in prevs[cur][1:]:
                roads[prev][cur] = -1
                if not deleted[prev]:
                    deleted[prev] = True
                    queue.append(prev)
        print(shortest_path(n, s, roads)[d][0])

if __name__ == "__main__":
    main()