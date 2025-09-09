import sys

input = sys.stdin.readline
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(w, h, map_, fire, man):
    burned = [[False] * w for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    fire_queue = fire
    man_queue = [man]
    for x, y in fire:
        burned[x][y] = True
    visited[man[0]][man[1]] = True
    count = 0
    while man_queue:
        count += 1
        nxt_fire_queue = []
        for fx, fy in fire_queue:
            for dx, dy in dirs:
                fnx, fny = fx + dx, fy + dy
                if not (0 <= fnx < h and 0 <= fny < w) or map_[fnx][fny] == '#' or burned[fnx][fny]:
                    continue
                burned[fnx][fny] = True
                nxt_fire_queue.append((fnx, fny))
        fire_queue = nxt_fire_queue
        nxt_man_queue = []
        for mx, my in man_queue:
            for dx, dy in dirs:
                mnx, mny = mx + dx, my + dy
                if not (0 <= mnx < h and 0 <= mny < w):
                    return count
                if map_[mnx][mny] == '#' or visited[mnx][mny] or burned[mnx][mny]:
                    continue
                visited[mnx][mny] = True
                nxt_man_queue.append((mnx, mny))
        man_queue = nxt_man_queue
    return "IMPOSSIBLE"


def main():
    t = int(input())
    for _ in range(t):
        w, h = map(int, input().split())
        map_ = []
        fire = []
        for i in range(h):
            line = input().rstrip()
            map_.append(line)
            for j in range(w):
                if line[j] == '*':
                    fire.append((i, j))
                elif line[j] == '@':
                    man = (i, j)
        print(bfs(w, h, map_, fire, man))


if __name__ == "__main__":
    main()
