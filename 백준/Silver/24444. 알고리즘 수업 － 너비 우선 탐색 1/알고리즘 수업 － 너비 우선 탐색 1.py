import sys
input = sys.stdin.readline

def bfs(n, adj_list, start):
    visited = [0] * (n+1)
    queue = [start]
    visited[start] = count = 1
    while queue:
        nxt_queue = []
        for cur in queue:
            for nxt in adj_list[cur]:
                if visited[nxt] == 0:
                    visited[nxt] = count = count + 1
                    nxt_queue.append(nxt)
        queue = nxt_queue
    return visited

def main():
    n, m, r = map(int, input().split())
    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    for i in range(1, n+1):
        adj_list[i].sort()
    visited = bfs(n, adj_list, r)
    print('\n'.join(map(str, visited[1:])))

if __name__ == "__main__":
    main()