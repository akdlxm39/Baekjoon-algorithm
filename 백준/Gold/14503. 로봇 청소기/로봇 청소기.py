import sys
input = sys.stdin.readline
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def robot(room, x, y, d):
    cnt, room[x][y] = 1, 2
    while True:
        for _ in range(4):
            d = (d+3)%4
            nx, ny = x + dx[d], y + dy[d]
            if room[nx][ny] == 0:
                x, y, room[nx][ny] = nx, ny, 2
                cnt += 1
                break
        else:
            x, y = x - dx[d], y - dy[d]
            if room[x][y] == 1:
                break
    return cnt

def main():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    print(robot(room, r, c, d))

if __name__ == "__main__":
    main()