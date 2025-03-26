import sys
from collections import deque
input = sys.stdin.readline

def bfs(n, m, k, maps):
    visited = [[-1]*m for _ in range(n)]
    queue = deque([(0, 0, 1, k)])
    visited[0][0] = k
    while queue:
        x, y, dist, can_break = queue.popleft()
        if visited[x][y] > can_break:
            continue
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x+dx, y+dy
            if not (0<=nx<n and 0<=ny<m) or can_break <= visited[nx][ny]:
                continue
            if nx == n-1 and ny == m-1:
                return dist+1
            nxt_can_break = can_break-(maps[nx][ny]=='1')
            visited[nx][ny] = nxt_can_break
            if nxt_can_break >= 0:
                queue.append((nx, ny, dist+1, nxt_can_break))
    return -1

def main():
    n, m, k = map(int, input().split())
    maps = [input().rstrip() for _ in range(n)]
    print(1 if n==1 and m==1 else bfs(n, m, k, maps))

if __name__ == "__main__":
    main()