import sys
from collections import deque
input = sys.stdin.readline

def bfs1(n, paint, visited, i, j):
    queue = deque([(i, j)])
    color = paint[i][j]
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not (0<=nx<n and 0<=ny<n) or visited[nx][ny] or paint[nx][ny] != color:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny))

def bfs2(n, paint, visited, i, j):
    queue = deque([(i, j)])
    color = paint[i][j]%2
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not (0<=nx<n and 0<=ny<n) or visited[nx][ny] or paint[nx][ny]%2 != color:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny))

def main():
    n = int(input())
    paint = [list(map(lambda x:{'R':0,'G':2,'B':1}[x], input().rstrip())) for _ in range(n)]
    cnt1, cnt2 = 0, 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            bfs1(n, paint, visited, i, j)
            cnt1 += 1
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            bfs2(n, paint, visited, i, j)
            cnt2 += 1
    print(cnt1, cnt2)

if __name__ == "__main__":
    main()