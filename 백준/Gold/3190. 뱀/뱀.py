import sys
input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def main():
    n = int(input())
    apples = [[False]*(n+1) for _ in range(n+1)]
    for _ in range(int(input())):
        x, y = map(int, input().split())
        apples[x][y] = True
    moves = dict()
    for _ in range(int(input())):
        x, c = input().split()
        moves[int(x)] = c
    snake = [(1, 1)]
    tail, sec, dir = 0, 1, 0
    while True:
        nx, ny = snake[-1][0] + dx[dir], snake[-1][1] + dy[dir]
        if not (0 < nx <= n and 0 < ny <= n) or (nx, ny) in snake[tail:]:
            break
        if apples[nx][ny]:
            apples[nx][ny] = False
        else:
            tail += 1
        snake.append((nx, ny))
        if sec in moves:
            dir = (dir + (1 if moves[sec] == 'D' else -1)) % 4
        sec += 1
    print(sec)

if __name__ == "__main__":
    main()