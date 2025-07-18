import sys

input = sys.stdin.readline
dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]
opposite = [0, 2, 1, 4, 3]


def move(k, colors, map_, horses):
    for i in range(k):
        x, y, c, d = horses[i]
        if colors[x + dx[d]][y + dy[d]] == 2:
            d = opposite[d]
            horses[i] = (x, y, c, d)
        nx, ny = x + dx[d], y + dy[d]
        if colors[nx][ny] != 2:
            tmp_horses = map_[x][y][c:]
            del map_[x][y][c:]
            nc = len(map_[nx][ny])
            if nc + len(tmp_horses) >= 4:
                return True
            if colors[nx][ny] == 1:
                tmp_horses.reverse()
            for h in tmp_horses:
                map_[nx][ny].append(h)
                horses[h] = (nx, ny, nc, horses[h][3])
                nc += 1
    return False


def main():
    n, k = map(int, input().split())
    colors = ([[2] * (n + 2)] +
              [[2] + list(map(int, input().split())) + [2] for _ in range(n)] +
              [[2] * (n + 2)])
    map_ = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
    horses = []
    for i in range(k):
        x, y, d = map(int, input().split())
        map_[x][y].append(i)
        horses.append((x, y, 0, d))

    for ans in range(1, 1001):
        if move(k, colors, map_, horses):
            print(ans)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()
