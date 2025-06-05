import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def make_tree(n, adj_list, parents, depths):
    queue = deque([1])
    depths[1] = 0
    while queue:
        cur = queue.popleft()
        for nxt, cost in adj_list[cur]:
            if depths[nxt] == -1:
                depths[nxt] = depths[cur] + 1
                parents[nxt][0] = [cur, cost]
                queue.append(nxt)
    for j in range(16):
        for i in range(1, n+1):
            parents[i][j+1][0] = parents[parents[i][j][0]][j][0]
            if parents[i][j+1][0] == 0: continue
            parents[i][j+1][1] = parents[i][j][1] + parents[parents[i][j][0]][j][1]
    return

def main():
    n = int(input())
    adj_list = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v, cost = map(int, input().split())
        adj_list[u].append((v, cost))
        adj_list[v].append((u, cost))
    parents = [[[0, 0] for _ in range(17)] for _ in range(n+1)]
    depths = [-1 for _ in range(n+1)]
    make_tree(n, adj_list, parents, depths)

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        total = 0
        if depths[a] < depths[b]:
            a, b = b, a
        while depths[a] != depths[b]:
            a, dist = parents[a][len(bin(depths[a] - depths[b]))-3]
            total += dist
        while a != b:
            i = len(bin(depths[a])) - 2
            while i > 0 and parents[a][i][0] == parents[b][i][0]:
                i -= 1
            [a, acost], [b, bcost] = parents[a][i], parents[b][i]
            total += acost + bcost
        print(total)


if __name__ == "__main__":
    main()