import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

def main():
    n, m = int(input()), int(input())
    adj_list = [dict() for _ in range(n+1)]
    for _ in range(m):
        s, e, cost = map(int, input().split())
        adj_list[s][e] = min(adj_list[s].get(e, INF), cost)
    start, end = map(int, input().split())
    costs = [INF] * (n+1)
    heap = [(0, start)]
    costs[start] = 0
    while heap:
        cost, cur = heappop(heap)
        if cur == end:
            break
        for nxt, nxt_cost in adj_list[cur].items():
            nxt_cost += cost
            if costs[nxt] > nxt_cost:
                costs[nxt] = nxt_cost
                heappush(heap, (nxt_cost, nxt))
    print(costs[end])

if __name__ == "__main__":
    main()