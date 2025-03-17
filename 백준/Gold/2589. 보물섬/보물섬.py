import sys
from collections import deque
input = sys.stdin.readline

delta = [(0,1), (0,-1), (1,0), (-1,0)]

def find(board, n, m, x, y):
    visited = [[False]*(m+2) for _ in range(n+2)]
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    while queue:
        cx, cy, dist = queue.popleft()
        for dx, dy in delta:
            nx, ny = cx+dx, cy+dy
            if visited[nx][ny] or board[nx][ny]=='W':
                continue
            visited[nx][ny] = True
            queue.append((nx, ny, dist+1))
    return dist

def main():
    n, m = map(int, input().split())
    board = ['W'*(m+2)] + ['W' + input().rstrip() + 'W' for _ in range(n)] + ['W'*(m+2)]
    ans = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] == 'L':
                ans = max(ans, find(board, n, m, i, j))
    print(ans)

if __name__ == "__main__":
    main()