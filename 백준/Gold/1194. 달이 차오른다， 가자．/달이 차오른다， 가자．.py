import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def bfs(n, m, maze, x, y):
    visited = [[[False]*64 for _ in range(m)] for _ in range(n)]
    queue = deque([(x, y, 0, 0)]) # x, y, dist, bitmask
    visited[x][y][0] = True
    while queue:
        cx, cy, dist, bitmask = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if not (0<=nx<n and 0<=ny<m) or visited[nx][ny][bitmask] or maze[nx][ny]=='#': continue
            if maze[nx][ny] == '1':
                return dist+1
            if 'A'<=maze[nx][ny]<='F' and not bitmask&(1<<(ord(maze[nx][ny])-65)):
                continue
            visited[nx][ny][bitmask] = True
            nxt_bitmask = bitmask
            if 'a' <= maze[nx][ny] <= 'f':
                nxt_bitmask |= (1 << (ord(maze[nx][ny]) - 97))
                visited[nx][ny][nxt_bitmask] = True
            queue.append((nx, ny, dist + 1, nxt_bitmask))
    return -1

def main():
    n, m = map(int, input().split())
    maze = [list(input().rstrip()) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '0':
                print(bfs(n, m, maze, i, j))
                return

if __name__ == "__main__":
    main()