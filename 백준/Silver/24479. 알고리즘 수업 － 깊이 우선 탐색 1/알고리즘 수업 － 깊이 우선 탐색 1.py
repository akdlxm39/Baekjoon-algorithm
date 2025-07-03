import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6+5)

def dfs(adj_list, visited, cur, count):
    visited[cur] = count
    for nxt in adj_list[cur]:
        if visited[nxt] == 0:
            count = dfs(adj_list, visited, nxt, count+1)
    return count

def main():
    n, m, r = map(int, input().split())
    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    for i in range(1, n+1):
        adj_list[i].sort()
    visited = [0]*(n+1)
    dfs(adj_list, visited, r, 1)
    print('\n'.join(map(str, visited[1:])))

if __name__ == "__main__":
    main()