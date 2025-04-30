import sys
from collections import deque

input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    maze = [list(map(int, input().rstrip())) for _ in range(n)]
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0<=nx<n and 0<=ny<m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx, ny))
    print(maze[n-1][m-1])


if __name__ == "__main__":
    main()