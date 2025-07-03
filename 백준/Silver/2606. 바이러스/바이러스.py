import sys
input = sys.stdin.readline

def bfs(n, adj_list, start):
    visited = [False] * (n+1)
    queue = [start]
    visited[start] = True
    while queue:
        nxt_queue = []
        for cur in queue:
            for nxt in adj_list[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    nxt_queue.append(nxt)
        queue = nxt_queue
    return sum(visited)

def main():
    n, m = int(input()), int(input())
    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)
    print(bfs(n, adj_list, 1)-1)

if __name__ == "__main__":
    main()