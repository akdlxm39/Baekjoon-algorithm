import sys
input = sys.stdin.readline
dx, dy = [[0, -1, 0, 1], [0, 1, 0, -1]], [1, 0, -1, 0]

def spread(r, c, room):
    dust = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if room[x][y] == -1: continue
            tmp = room[x][y] // 5
            if tmp == 0: continue
            for i in range(4):
                nx, ny = x + dx[0][i], y + dy[i]
                if not (0 <= nx < r and 0 <= ny < c) or room[nx][ny] == -1: continue
                dust[nx][ny] += tmp
                room[x][y] -= tmp
    for x in range(r):
        for y in range(c):
            room[x][y] += dust[x][y]

def purify(r, c, room, air_purifier):
    for i in range(2):
        x, y = air_purifier[i], 0
        tmp = 0
        for j in range(4):
            while True:
                nx, ny = x + dx[i][j], y + dy[j]
                if not (0 <= nx < r and 0 <= ny < c) or room[nx][ny] == -1: break
                x, y = nx, ny
                room[x][y], tmp = tmp, room[x][y]

def main():
    r, c, t = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(r)]
    air_purifier = ()
    for i in range(r):
        if room[i][0] == -1:
            air_purifier = (i, i + 1)
            break
    for _ in range(t):
        spread(r, c, room)
        purify(r, c, room, air_purifier)
    print(sum(sum(r) for r in room) + 2)


if __name__ == "__main__":
    main()