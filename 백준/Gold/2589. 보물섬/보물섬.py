import sys
from collections import deque
input = sys.stdin.readline

delta = [(0,1), (0,-1), (1,0), (-1,0)]

def find1(board, visited, x, y):
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    end_point = []
    while queue:
        cx, cy, dist = queue.popleft()
        end_flag = True
        for dx, dy in delta:
            nx, ny = cx+dx, cy+dy
            if board[nx][ny]=='W' or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny, dist+1))
            end_flag = False
        if end_flag:
            end_point.append((cx, cy))
    return end_point

def find2(board, x, y):
    visited = [[False]*len(board[0]) for _ in range(len(board))]
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    dist = 0
    while queue:
        cx, cy, dist = queue.popleft()
        for dx, dy in delta:
            nx, ny = cx+dx, cy+dy
            if board[nx][ny]=='W' or visited[nx][ny]:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny, dist+1))
    return dist

def main():
    n, m = map(int, input().split())
    board = [['W']*(m+2)] + [['W'] + list(input().rstrip()) + ['W'] for _ in range(n)] + [['W']*(m+2)]
    visited = [[False]*(m+2) for _ in range(n+2)]
    points = []
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i][j] == 'L' and not visited[i][j]:
                points += find1(board, visited, i, j)
    ans = 0
    for i, j in points:
        ans = max(ans, find2(board, i, j))
    print(ans)

if __name__ == "__main__":
    main()