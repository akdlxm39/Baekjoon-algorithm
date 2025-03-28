import sys
from collections import deque
input = sys.stdin.readline

def bfs(adj_list, groups, x):
    queue = deque([x])
    groups[x] = 1
    while queue:
        cur = queue.popleft()
        for nxt in adj_list[cur]:
            if not groups[nxt]:
                groups[nxt] = 3-groups[cur]
                queue.append(nxt)
            elif groups[nxt] == groups[cur]:
                return False
    return True

def main():
    k = int(input())
    for _ in range(k):
        vertex, edge = map(int, input().split())
        adj_list = dict()
        for _ in range(edge):
            u, v = map(int, input().split())
            if u not in adj_list:
                adj_list[u] = []
            if v not in adj_list:
                adj_list[v] = []
            adj_list[u].append(v)
            adj_list[v].append(u)
        groups = [0]*(vertex+1)
        for i in adj_list.keys():
            if groups[i]:
                continue
            if not bfs(adj_list, groups, i):
                print("NO")
                break
        else:
            print("YES")

if __name__ == "__main__":
    main()