import sys
from collections import deque

input = sys.stdin.readline
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def move(board, x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs(n, m, board, rx, ry, bx, by):
    queue = [(rx, ry, bx, by)]
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    for cnt in range(1, 11):
        next_queue = []
        for rcx, rcy, bcx, bcy in queue:
            for dx, dy in dir:
                rnx, rny, rcnt = move(board, rcx, rcy, dx, dy)
                bnx, bny, bcnt = move(board, bcx, bcy, dx, dy)
                if board[bnx][bny] == 'O':
                    continue
                if board[rnx][rny] == 'O':
                    return cnt
                if rnx == bnx and rny == bny:
                    if rcnt > bcnt:
                        rnx -= dx
                        rny -= dy
                    else:
                        bnx -= dx
                        bny -= dy
                if visited[rnx][rny][bnx][bny]:
                    continue
                visited[rnx][rny][bnx][bny] = True
                next_queue.append((rnx, rny, bnx, bny))
        queue = next_queue
    return -1


def main():
    n, m = map(int, input().split())
    board = [input().rstrip() for _ in range(n)]
    rx = ry = bx = by = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rx, ry = i, j
            elif board[i][j] == 'B':
                bx, by = i, j
    print(bfs(n, m, board, rx, ry, bx, by))


if __name__ == "__main__":
    main()
