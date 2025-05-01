import sys
input = sys.stdin.readline
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def robot(room, x, y, d):
    cnt, flag = 0, True
    while True:
        if room[x][y] == 0:
            room[x][y] = 2
            cnt += 1
            continue
        if flag:
            for i in range(4):
                if room[x+dx[i]][y+dy[i]] == 0: break
            else: flag = False
        if flag:
            d = (d + 3) % 4
            nx, ny = x + dx[d], y + dy[d]
            if room[nx][ny] == 0: x, y = nx, ny
        else:
            nx, ny = x - dx[d], y - dy[d]
            if room[nx][ny] == 1: break
            else: x, y, flag = nx, ny, True
    return cnt

def main():
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    print(robot(room, r, c, d))

if __name__ == "__main__":
    main()