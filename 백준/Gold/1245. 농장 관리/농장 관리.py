import sys
from collections import deque
from itertools import product
input = sys.stdin.readline

def solve(n, m, farm, visited, queue):
    flag = 1
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for dx, dy in product([-1, 0, 1], repeat=2):
            nx, ny = x + dx, y + dy
            if (dx == 0 and dy == 0) or not (0 <= nx < n and 0 <= ny < m):
                continue
            if not visited[nx][ny] and farm[nx][ny] == farm[x][y]:
                queue.append((nx, ny))
            elif farm[nx][ny] > farm[x][y]:
                flag = 0
    return flag

def main():
    n, m = map(int, input().split())
    farm = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                continue
            queue.append((i, j))
            cnt += solve(n, m, farm, visited, queue)
    print(cnt)

if __name__ == "__main__":
    main()