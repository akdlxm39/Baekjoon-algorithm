import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, m, box, visited):
    ans = 0
    cnt = 0
    queue = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                continue
            visited[i][j] = True
            cnt += 1
            if box[i][j] == 1:
                queue.append((i, j, 0))
    if cnt == n * m:
        return 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        cx, cy, day = queue.popleft()
        ans = day
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            cnt += 1
            queue.append((nx, ny, day + 1))
    if cnt == n * m:
        return ans
    return -1

def main():
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    print(bfs(n, m, box, visited))

if __name__ == "__main__":
    main()