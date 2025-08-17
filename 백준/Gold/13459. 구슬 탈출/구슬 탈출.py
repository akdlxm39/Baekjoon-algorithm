import sys
from collections import deque

input = sys.stdin.readline
dictionary = {'.': 0, '#': 1, 'R': 2, 'B': 3, 'O': 4}
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs(board, red, blue, goal):
    queue = deque([(red, blue)])
    visited = {(red, blue)}
    for _ in range(10):
        nxt_queue = []
        for (rx, ry), (bx, by) in queue:
            for i in range(4):
                rcx, rcy, bcx, bcy = rx, ry, bx, by
                bmove, state = True, 0
                while True:
                    bnx, bny = bcx + dx[i], bcy + dy[i]
                    if board[bnx][bny]:
                        bmove = False
                        break
                    elif bnx == goal[0] and bny == goal[1]:
                        state = 1
                        break
                    elif bnx == rcx and bny == rcy:
                        break
                    bcx, bcy = bnx, bny
                if state == 1: continue
                while True:
                    rnx, rny = rcx + dx[i], rcy + dy[i]
                    if board[rnx][rny]:
                        break
                    elif rnx == goal[0] and rny == goal[1]:
                        rcx, rcy = rnx, rny
                        state = 2
                        break
                    elif rnx == bcx and rny == bcy:
                        break
                    rcx, rcy = rnx, rny
                while bmove:
                    bnx, bny = bcx + dx[i], bcy + dy[i]
                    if board[bnx][bny]:
                        break
                    elif bnx == goal[0] and bny == goal[1]:
                        state = 1
                        break
                    elif bnx == rcx and bny == rcy:
                        break
                    bcx, bcy = bnx, bny
                if state == 1:
                    continue
                elif state == 2:
                    return True
                nxt = ((rcx, rcy), (bcx, bcy))
                if nxt in visited: continue
                nxt_queue.append(nxt)
                visited.add(nxt)
        queue = nxt_queue
    return False


def main():
    n, m = map(int, input().split())
    board = []
    red, blue, goal = None, None, None
    for i in range(n):
        line = []
        for j, x in enumerate(input().rstrip()):
            line.append(1 if x == '#' else 0)
            if x == 'R':
                red = (i, j)
            elif x == 'B':
                blue = (i, j)
            elif x == 'O':
                goal = (i, j)
        board.append(line)
    print(1 if bfs(board, red, blue, goal) else 0)


if __name__ == "__main__":
    main()
