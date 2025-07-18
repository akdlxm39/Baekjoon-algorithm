import sys
from itertools import combinations

input = sys.stdin.readline
dx, dy = [0, -1, 0], [-1, 0, 1]

def bfs(n, m, d, board, archers, x):
    shoot = set()
    for y in archers:
        if board[x][y] == 1:
            shoot.add((x, y))
            continue
        queue = [(x, y)]
        visited = [[False] * m for _ in range(n)]
        visited[x][y] = True
        for _ in range(d - 1):
            flag = False
            nxt_queue = []
            for cx, cy in queue:
                for i in range(3):
                    nx, ny = cx + dx[i], cy + dy[i]
                    if not (0 <= nx and 0 <= ny < m) or visited[nx][ny]: continue
                    if board[nx][ny] == 1:
                        shoot.add((nx, ny))
                        flag = True
                        break
                    visited[nx][ny] = True
                    nxt_queue.append((nx, ny))
                if flag:
                    break
            if flag:
                break
            queue = nxt_queue
    for x, y in shoot:
        board[x][y] = 0
    return len(shoot)

def main():
    n, m, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for archers in combinations(range(m), 3):
        tmp = 0
        tmp_board = [b.copy() for b in board]
        for x in range(n-1, -1, -1):
            tmp += bfs(n, m, d, tmp_board, archers, x)
        ans = max(ans, tmp)
    print(ans)

if __name__ == "__main__":
    main()
