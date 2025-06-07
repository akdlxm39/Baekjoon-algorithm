import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def main():
    n, m, k = map(int, input().split())
    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, cost = map(int, input().split())
        adj_list[u].append((v, cost))
    count = [0]*(n+1)
    dist = [-1]*(n+1)
    heap = [(0, 1)]
    while heap:
        cur_dist, cur = heappop(heap)
        if count[cur] == k: continue
        count[cur] += 1
        dist[cur] = cur_dist
        for nxt, nxt_cost in adj_list[cur]:
            if count[nxt] == k: continue
            nxt_dist = cur_dist + nxt_cost
            heappush(heap, (nxt_dist, nxt))

    for i in range(1, n+1):
        if count[i] == k:
            print(dist[i])
        else:
            print(-1)

if __name__ == "__main__":
    main()