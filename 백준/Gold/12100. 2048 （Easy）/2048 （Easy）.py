import sys

input = sys.stdin.readline
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
start_dir = [(1, 0), (0, 1), (1, 0), (0, 1)]


def move(n, board, start, d):
    x, y = start[d]
    while x < n and y < n:
        line = []
        cx, cy = x, y
        while 0 <= cx < n and 0 <= cy < n:
            if board[cx][cy]:
                if line and line[-1] == board[cx][cy]:
                    line[-1] *= -2
                else:
                    line.append(board[cx][cy])
            cx += dir[d][0]
            cy += dir[d][1]
        idx = 0
        cx, cy = x, y
        while 0 <= cx < n and 0 <= cy < n:
            if idx < len(line):
                board[cx][cy] = abs(line[idx])
                idx += 1
            else:
                board[cx][cy] = 0
            cx += dir[d][0]
            cy += dir[d][1]
        x += start_dir[d][0]
        y += start_dir[d][1]


def dfs(n, board, start, cnt):
    if cnt == 5:
        return max(max(line) for line in board)
    res = []
    for d in range(4):
        next_board = [board[i][:] for i in range(n)]
        move(n, next_board, start, d)
        res.append(dfs(n, next_board, start, cnt + 1))
    return max(res)


def main():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    start = [(0, 0), (0, 0), (0, n - 1), (n - 1, 0)]
    print(dfs(n, board, start, 0))


if __name__ == "__main__":
    main()
