import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, cost = map(int, input().split())
        adj_list[s].append((e, cost))
    start, end = map(int, input().split())
    costs = [-1] * (n+1)
    heap = [(0, start)]
    while heap:
        cost, cur = heappop(heap)
        if costs[cur] != -1:
            continue
        costs[cur] = cost
        if cur == end:
            break
        for nxt, nxt_cost in adj_list[cur]:
            if costs[nxt] != -1:
                continue
            heappush(heap, (cost + nxt_cost, nxt))
    print(costs[end])

if __name__ == "__main__":
    main()