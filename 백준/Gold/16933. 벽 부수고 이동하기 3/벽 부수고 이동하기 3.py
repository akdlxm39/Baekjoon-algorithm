import sys

input = sys.stdin.readline


def bfs(n, m, k, maze):
    dx = [-1, 1, -m, m]
    visited = [-1] * (n * m - 1)
    visited[0] = k
    queue = [(0, k)]
    nxt_queue = []
    time = 1
    while (queue or nxt_queue) and visited[-1] == -1:
        time += 1
        nxt_nxt_queue = []
        for cx, ck in queue:
            for i in range(4):
                nx = cx + dx[i]
                if maze[nx] == '2': continue
                nk = ck - (maze[nx] == '1')
                if visited[nx] >= nk: continue
                visited[nx] = nk
                if maze[nx] == '1' and time % 2:
                    nxt_nxt_queue.append((nx, nk))
                else:
                    nxt_queue.append((nx, nk))
        queue, nxt_queue = nxt_queue, nxt_nxt_queue

    return time if visited[-1] != -1 else -1


def main():
    n, m, k = map(int, input().split())
    maze = ''
    for _ in range(n):
        maze += input().rstrip() + '2'
    maze += '2' * m
    print(1 if n == 1 and m == 1 else bfs(n, m + 1, k, maze))


if __name__ == "__main__":
    main()
