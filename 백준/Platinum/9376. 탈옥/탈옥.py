import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(h, w, jail, x, y):
    queue = deque([(0, x, y)])
    count = [[INF] * w for _ in range(h)]
    count[x][y] = 0
    while queue:
        cnt, cx, cy = queue.popleft()
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if jail[nx][ny] == '*' or count[nx][ny] != INF:
                continue
            if jail[nx][ny] == '#':
                count[nx][ny] = cnt + 1
                queue.append((cnt + 1, nx, ny))
            else:
                count[nx][ny] = cnt
                queue.appendleft((cnt, nx, ny))
    return count


def add(h, w, count, delta):
    for i in range(h):
        for j in range(w):
            count[i][j] += delta[i][j]


def main():
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        jail = (['.' * (w + 2)] +
                ['.' + input().rstrip() + '.' for _ in range(h)] +
                ['.' * (w + 2)])
        h += 2
        w += 2
        count = bfs(h, w, jail, 0, 0)
        for i in range(h):
            for j in range(w):
                if jail[i][j] == '$':
                    add(h, w, count, bfs(h, w, jail, i, j))
                elif jail[i][j] == '#':
                    count[i][j] -= 2
        print(min(min(line) for line in count))


if __name__ == "__main__":
    main()
