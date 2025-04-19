import sys
input = sys.stdin.readline

def get_tree_about_level(n, adj_list, root):
    tree_about_level = [[root]]
    visited = [False]*(n+1)
    visited[root] = True
    parent = [0]*(n+1)
    level = 0
    while level < len(tree_about_level):
        tmp = []
        for cur in tree_about_level[level]:
            for nxt in adj_list[cur]:
                if visited[nxt]:
                    continue
                visited[nxt] = True
                tmp.append(nxt)
                parent[nxt] = cur
        if tmp:
            tree_about_level.append(tmp)
        level += 1
    return tree_about_level, parent


def dfs(tree, parent, dp_sum, dp_set):
    for line in tree[:0:-1]:
        for cur in line:
            if dp_sum[cur][0] > dp_sum[cur][1]:
                dp_sum[parent[cur]][0] += dp_sum[cur][0]
                dp_set[parent[cur]][0].extend(dp_set[cur][0])
            else:
                dp_sum[parent[cur]][0] += dp_sum[cur][1]
                dp_set[parent[cur]][0].extend(dp_set[cur][1])
            dp_sum[parent[cur]][1] += dp_sum[cur][0]
            dp_set[parent[cur]][1].extend(dp_set[cur][0])

def main():
    n = int(input())
    weights = list(map(int, input().split()))
    adj_list = [[] for _ in range(n + 1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    root = 1
    tree, parent = get_tree_about_level(n, adj_list, root)
    dp_sum = [[0,0]] + [[0, weight] for weight in weights]
    dp_set = [[[],[]]] + [[[],[i]] for i in range(1, n+1)]
    dfs(tree, parent, dp_sum, dp_set)
    if dp_sum[root][0]>=dp_sum[root][1]:
        print(dp_sum[root][0])
        print(*sorted(dp_set[root][0]))
    else:
        print(dp_sum[root][1])
        print(*sorted(dp_set[root][1]))

if __name__ == "__main__":
    main()