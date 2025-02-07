import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]
    in_degree = [0] * (n+1)
    heap = []
    ans = []
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        in_degree[b] += 1
    for i in range(1, n+1):
        if in_degree[i] == 0:
            heappush(heap, i)
    while heap:
        cur = heappop(heap)
        ans.append(cur)
        for nxt in adj[cur]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                heappush(heap, nxt)
    print(*ans)

if __name__ == "__main__":
    main()