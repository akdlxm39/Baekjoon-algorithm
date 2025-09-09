import sys

input = sys.stdin.readline
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(w, h, map_, fire, mx, my):
    visited = [[0] * w for _ in range(h)]
    queue = []
    for x, y in fire:
        queue.append((2, x, y))
        visited[x][y] = 2
    queue.append((1, mx, my))
    visited[mx][my] = 1
    count = 0
    while queue and queue[-1][0] == 1:
        count += 1
        nxt_queue = []
        for cur, x, y in queue:
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < h and 0 <= ny < w):
                    if cur == 1:
                        return count
                    continue
                if map_[nx][ny] == '#' or visited[nx][ny] >= cur:
                    continue
                visited[nx][ny] = cur
                nxt_queue.append((cur, nx, ny))
        queue = nxt_queue
    return "IMPOSSIBLE"


def main():
    t = int(input())
    for _ in range(t):
        w, h = map(int, input().split())
        map_ = []
        fire = []
        x = y = 0
        for i in range(h):
            line = input().rstrip()
            map_.append(line)
            for j in range(w):
                if line[j] == '*':
                    fire.append((i, j))
                elif line[j] == '@':
                    x, y = i, j
        print(bfs(w, h, map_, fire, x, y))


if __name__ == "__main__":
    main()
