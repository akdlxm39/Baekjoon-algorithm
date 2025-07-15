import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(n, arr):
    queue = deque([(0, 0, arr[0][0], arr[0][0])])
    visited = [[[201]*201 for _ in range(n)] for _ in range(n)]
    visited[0][0][arr[0][0]] = arr[0][0]
    while queue:
        cx, cy, cmin, cmax = queue.popleft()
        if visited[cx][cy][cmin] < cmax: continue
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < n and 0 <= ny < n): continue
            nmin, nmax = min(cmin, arr[nx][ny]), max(cmax, arr[nx][ny])
            if visited[nx][ny][nmin] <= nmax: continue
            visited[nx][ny][nmin] = nmax
            queue.append((nx, ny, nmin, nmax))
    return min(visited[-1][-1][i] - i for i in range(201) if visited[-1][-1][i] != 201)

def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(bfs(n, arr))

if __name__ == "__main__":
    main()