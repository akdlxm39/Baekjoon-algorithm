import sys
from collections import deque
input = sys.stdin.readline

def make_tree(n, root):
    friends = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        friends[u].append(v)
        friends[v].append(u)
    tree_by_level = [[root]]
    parents = [0]*(n+1)
    visited = [False] * (n + 1)
    visited[root] = True
    i = 0
    while i < len(tree_by_level):
        tmp =[]
        for cur in tree_by_level[i]:
            for nxt in friends[cur]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                tmp.append(nxt)
                parents[nxt] = cur
        if tmp:
            tree_by_level.append(tmp)
        i += 1
    return tree_by_level, parents

def main():
    n = int(input())
    root = 1
    tree_by_level, parents = make_tree(n, root)
    dp = [[0, 1] for _ in range(n + 1)]
    for i in range(len(tree_by_level)-1, -1, -1):
        for cur in tree_by_level[i]:
            dp[parents[cur]][0] += dp[cur][1]
            dp[parents[cur]][1] += min(dp[cur])
    print(min(dp[root]))

if __name__ == "__main__":
    main()