import sys
from collections import deque

input = sys.stdin.readline
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = int(1e9)


def bfs_water(r, c, forest, waters, watered_forest):
    while waters:
        time, cx, cy = waters.popleft()
        time += 1
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < r and 0 <= ny < c) or forest[nx][ny] == 'X':
                continue
            if forest[nx][ny] == 'D': continue
            if watered_forest[nx][ny] <= time:
                continue
            watered_forest[nx][ny] = time
            waters.append((time, nx, ny))


def bfs(r, c, forest, watered_forest, x, y):
    queue = deque([(0, x, y)])
    visited = [[False] * c for _ in range(r)]
    visited[x][y] = True
    while queue:
        time, cx, cy = queue.popleft()
        time += 1
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < r and 0 <= ny < c) or forest[nx][ny] == 'X':
                continue
            if forest[nx][ny] == 'D':
                return time
            if visited[nx][ny] or watered_forest[nx][ny] <= time:
                continue
            visited[nx][ny] = True
            queue.append((time, nx, ny))
    return 'KAKTUS'


def main():
    r, c = map(int, input().split())
    forest = [input().rstrip() for _ in range(r)]
    waters = deque()
    watered_forest = [[INF] * c for _ in range(r)]
    sx = sy = 0
    for i in range(r):
        for j in range(c):
            if forest[i][j] == '*':
                waters.append((0, i, j))
                watered_forest[i][j] = 0
            elif forest[i][j] == 'S':
                sx, sy = i, j
    bfs_water(r, c, forest, waters, watered_forest)
    print(bfs(r, c, forest, watered_forest, sx, sy))


if __name__ == "__main__":
    main()
