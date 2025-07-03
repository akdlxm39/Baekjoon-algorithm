import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6+5)

# def dfs1(adj_list, visited, cur, count):
#     visited[cur] = count
#     for nxt in adj_list[cur]:
#         if visited[nxt] == 0:
#             count = dfs1(adj_list, visited, nxt, count + 1)
#     return count

def dfs2(n, adj_list, start):
    visited = [0]*(n+1)
    stack = [start]
    count = 1
    while stack:
        cur = stack.pop()
        if visited[cur] == 0:
            visited[cur] = count
            count += 1
            stack.extend(adj_list[cur])
    return visited

def main():
    n, m, r = map(int, input().split())
    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    for i in range(1, n+1):
        adj_list[i].sort(reverse=True)
    # visited = [0]*(n+1)
    # dfs1(adj_list, visited, r, 1)
    visited = dfs2(n, adj_list, r)
    print('\n'.join(map(str, visited[1:])))

if __name__ == "__main__":
    main()