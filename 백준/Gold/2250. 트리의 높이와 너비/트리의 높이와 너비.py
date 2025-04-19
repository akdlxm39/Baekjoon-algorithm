import sys
from collections import deque
input = sys.stdin.readline

def get_depths(n, root, tree):
    queue = deque([root])
    depths = [0] * (n + 1)
    depths[root] = 1
    while queue:
        cur = queue.popleft()
        for nxt in tree[cur]:
            if nxt == -1 or depths[nxt]:
                continue
            depths[nxt] = depths[cur] + 1
            queue.append(nxt)
    return depths

def dfs(tree, depths, cur, idx, array):
    if tree[cur][0] != -1:
        idx = dfs(tree, depths, tree[cur][0], idx, array) + 1
    array[depths[cur]].append(idx)
    if tree[cur][1] != -1:
        idx = dfs(tree, depths, tree[cur][1], idx+1, array)
    return idx

def main():
    n = int(input())
    tree = dict()
    root = n*(n+1)//2
    for _ in range(n):
        cur, left, right = map(int, input().split())
        tree[cur] = (left, right)
        root -= left if left != -1 else 0
        root -= right if right != -1 else 0
    depths = get_depths(n, root, tree)
    array = [[] for _ in range(max(depths)+1)]
    dfs(tree, depths, root, 1, array)
    level, max_gap = 0, 0
    for i, x in enumerate(array[1:], 1):
        gap = max(x)-min(x)+1
        if gap > max_gap:
            max_gap = gap
            level = i
    print(level, max_gap)

if __name__ == "__main__":
    main()