import sys
from collections import deque
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def move(board, snake, dir):
    nx, ny = snake[0][0] + dx[dir], snake[0][1] + dy[dir]
    if board[nx][ny] == 1:
        return False
    if board[nx][ny] != 2:
        rx, ry = snake.pop()
        board[rx][ry] = 0
    snake.appendleft((nx, ny))
    board[nx][ny] = 1
    return True

def main():
    n = int(input())
    n += 2
    board = [[0]*n for _ in range(n)]
    for i in range(n):
        board[0][i] = board[n-1][i] = board[i][0] = board[i][n-1] = 1
    for _ in range(int(input())):
        x, y = map(int, input().split())
        board[x][y] = 2
    board[1][1] = 1
    snake = deque([(1, 1)])
    sec, dir = 1, 0
    for _ in range(int(input())):
        x, c = input().split()
        x = int(x)+1
        for s in range(sec, x):
            if not move(board, snake, dir):
                sec = s
                break
        else:
            dir = (dir + (1 if c == 'D' else -1)) % 4
            sec = x
            continue
        break
    else:
        while True:
            if not move(board, snake, dir):
                break
            sec += 1
    print(sec)

if __name__ == "__main__":
    main()