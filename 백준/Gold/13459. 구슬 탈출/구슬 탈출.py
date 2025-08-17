import sys
from collections import deque

input = sys.stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def move(board, x, y, dx_, dy_):
    cnt = 0
    while board[x + dx_][y + dy_] != '#' and board[x][y] != 'O':
        x += dx_
        y += dy_
        cnt += 1
    return cnt, x, y


def bfs(board, start):
    queue = [start]
    visited = {start}
    for _ in range(10):
        nxt_queue = []
        for rx, ry, bx, by in queue:
            for i in range(4):
                rcnt, rnx, rny = move(board, rx, ry, dx[i], dy[i])
                bcnt, bnx, bny = move(board, bx, by, dx[i], dy[i])
                if board[bnx][bny] == 'O': continue
                if board[rnx][rny] == 'O': return 1
                if rnx == bnx and rny == bny:
                    if rcnt > bcnt:
                        rnx -= dx[i]
                        rny -= dy[i]
                    else:
                        bnx -= dx[i]
                        bny -= dy[i]
                nxt = (rnx, rny, bnx, bny)
                if nxt in visited: continue
                nxt_queue.append(nxt)
                visited.add(nxt)
        queue = nxt_queue
    return 0


def main():
    n, m = map(int, input().split())
    board = [input().rstrip() for _ in range(n)]
    start = [0, 0, 0, 0]
    for i in range(n):
        if 'R' in board[i]:
            start[0], start[1] = i, board[i].index('R')
        if 'B' in board[i]:
            start[2], start[3] = i, board[i].index('B')
    print(bfs(board, tuple(start)))


if __name__ == "__main__":
    main()
