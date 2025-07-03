import sys
input = sys.stdin.readline

def dfs(n, adj_list, start):
    visited = [0]*(n+1)
    stack = [start]
    res = []
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            visited[cur] = True
            res.append(cur)
            stack.extend(reversed(adj_list[cur]))
    return res

def bfs(n, adj_list, start):
    visited = [False] * (n+1)
    queue = [start]
    res = []
    visited[start] = True
    while queue:
        res.extend(queue)
        nxt_queue = []
        for cur in queue:
            for nxt in adj_list[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    nxt_queue.append(nxt)
        queue = nxt_queue
    return res

def main():
    n, m, v = map(int, input().split())
    adj_list = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    for i in range(1, n+1):
        adj_list[i].sort()
    print(' '.join(map(str, dfs(n, adj_list, v))))
    print(' '.join(map(str, bfs(n, adj_list, v))))

if __name__ == "__main__":
    main()