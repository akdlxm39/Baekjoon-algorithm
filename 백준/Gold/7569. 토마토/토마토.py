import sys
from collections import deque
input = sys.stdin.readline
dx, dy, dz = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]

def bfs(m, n, h, tomatoes):
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomatoes[i][j][k] == 1:
                    queue.append((i, j, k, 0))
    day = -1
    while queue:
        x, y, z, day = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if not (0<=nx<h and 0<=ny<n and 0<=nz<m) or tomatoes[nx][ny][nz] != 0:
                continue
            tomatoes[nx][ny][nz] = 1
            queue.append((nx, ny, nz, day+1))
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomatoes[i][j][k] == 0:
                    return -1
    return day

def main():
    m, n, h = map(int, input().split())
    tomatoes = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    print(bfs(m, n, h, tomatoes))

if __name__ == "__main__":
    main()