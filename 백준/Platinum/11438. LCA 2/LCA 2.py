import sys
from collections import deque
input = sys.stdin.readline

def make_tree(n, adj_list, parents, depths):
    queue = deque([(1, 0)])
    while queue:
        cur, depth = queue.popleft()
        depths[cur] = depth
        for nxt in adj_list[cur]:
            if depths[nxt] == -1:
                parents[nxt][0] = cur
                queue.append((nxt, depth+1))
    for j in range(19):
        for i in range(1, n+1):
            parents[i][j+1] = parents[parents[i][j]][j]

def main():
    n = int(input())
    adj_list = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    parents = [[0] * 20 for _ in range(n + 1)]
    depths = [-1] * (n + 1)
    make_tree(n, adj_list, parents, depths)
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if depths[a] < depths[b]:
            a, b = b, a
        while depths[a] != depths[b]:
            a = parents[a][len(bin(depths[a] - depths[b]))-3]
        while a!=b:
            i = len(bin(depths[a]))-2
            while i > 0 and parents[a][i]==parents[b][i]:
                i -= 1
            a, b = parents[a][i], parents[b][i]
        print(a)

if __name__ == "__main__":
    main()