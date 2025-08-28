import sys
from collections import deque

input = sys.stdin.readline
dir_change = [-1, 1, 3, 0, 2]
dir = [[(-1, 0), (-1, 1), (-1, -1)],  # 3
       [(0, 1), (1, 1), (-1, 1)],  # 1
       [(1, 0), (1, -1), (1, 1)],  # 4
       [(0, -1), (-1, -1), (1, -1)]]  # 2
dir_ = [(0, 1, 1), (1, 0, 2)]


def heating(r, c, wall, temp_delta, x, y, d):
    heater = [(x + dir[d][0][0], y + dir[d][0][1], d)]
    visited = set()
    for t in range(5, 0, -1):
        next_heater = []
        for x, y, d in heater:
            temp_delta[x][y] += t
            for di in range(-1, 2, 1):
                dx, dy = dir[d][di]
                nx, ny = x + dx, y + dy
                if not (0 <= nx < r and 0 <= ny < c):
                    continue
                if (nx, ny) in visited:
                    continue
                if wall[x][y][(d + di) % 4] or wall[nx][ny][(d + 2) % 4]:
                    continue
                visited.add((nx, ny))
                next_heater.append((nx, ny, d))
        heater = next_heater


def get_temp_delta_checker(r, c, room, wall):
    temp_delta = [[0] * c for _ in range(r)]
    checker = []
    for i in range(r):
        for j in range(c):
            if room[i][j] == 0:
                continue
            elif room[i][j] == 5:
                checker.append((i, j))
                continue
            heating(r, c, wall, temp_delta, i, j, dir_change[room[i][j]])

    return temp_delta, checker


def room_sum(r, c, temp, delta):
    for i in range(r):
        for j in range(c):
            temp[i][j] += delta[i][j]


def cycle(r, c, temp, temp_delta, wall):
    room_sum(r, c, temp, temp_delta)
    temp_tmp = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            for dx, dy, d in dir_:
                if wall[x][y][d]:
                    continue
                nx, ny = x + dx, y + dy
                if nx == r or ny == c:
                    continue
                move = int((temp[x][y] - temp[nx][ny]) / 4)
                temp_tmp[x][y] -= move
                temp_tmp[nx][ny] += move
    room_sum(r, c, temp, temp_tmp)
    for i in range(r):
        if temp[i][0]:
            temp[i][0] -= 1
        if temp[i][-1]:
            temp[i][-1] -= 1
    for i in range(1, c - 1):
        if temp[0][i]:
            temp[0][i] -= 1
        if temp[-1][i]:
            temp[-1][i] -= 1


def check(temp, checker, k):
    for x, y in checker:
        if temp[x][y] < k:
            return False
    return True


def main():
    r, c, k = map(int, input().split())
    room = [[x for x in map(int, input().split())] for _ in range(r)]
    wall = [[[False] * 4 for _ in range(c)] for _ in range(r)]
    w = int(input())
    for _ in range(w):
        x, y, t = map(int, input().split())
        if t == 0:
            wall[x - 1][y - 1][0] = True
            wall[x - 2][y - 1][2] = True
        elif t == 1:
            wall[x - 1][y - 1][1] = True
            wall[x - 1][y][3] = True
    temp_delta, checker = get_temp_delta_checker(r, c, room, wall)
    temp = [[0] * c for _ in range(r)]
    for i in range(1, 101):
        cycle(r, c, temp, temp_delta, wall)
        if check(temp, checker, k):
            print(i)
            break
    else:
        print(101)


if __name__ == "__main__":
    main()
