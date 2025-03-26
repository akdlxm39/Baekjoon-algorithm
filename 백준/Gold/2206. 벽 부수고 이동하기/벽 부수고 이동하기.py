import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, m, maps):
    visited = [[0]*m for _ in range(n)]
    queue = deque([(0, 0, 1, True)])
    visited[0][0] = 2
    while queue:
        x, y, dist, can_break = queue.popleft()
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if nx == n-1 and ny == m-1:
                return dist+1
            elif not (0<=nx<n and 0<=ny<m) or visited[nx][ny] == 2:
                continue
            if can_break:
                visited[nx][ny] = 2
                queue.append((nx, ny, dist+1, maps[nx][ny]==0))
            elif visited[nx][ny]==0 and maps[nx][ny]==0:
                visited[nx][ny] = 1
                queue.append((nx, ny, dist+1, False))
    return -1

def main():
    n, m = map(int, input().split())
    maps = [list(map(int, list(input().rstrip()))) for _ in range(n)]
    print(1 if n==1 and m==1 else bfs(n, m, maps))

if __name__ == "__main__":
    main()