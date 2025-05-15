import sys
from collections import deque
input = sys.stdin.readline

def fire_route(maze, fired, fires):
    queue = deque(fires)
    for fx, fy in fires:
        fired[fx][fy] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if fired[nx][ny] != -1 or maze[nx][ny] == '#' or maze[nx][ny] == '@':
                continue
            fired[nx][ny] = fired[x][y] + 1
            queue.append((nx, ny))

def escape_route(maze, fired, j):
    queue = deque([(j[0], j[1], 1)])
    while queue:
        x, y, day = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if maze[nx][ny] == '@':
                return day
            if maze[nx][ny] == '#' or -1 < fired[nx][ny] <= day:
                continue
            fired[nx][ny] = 0
            queue.append((nx, ny, day+1))
    return 'IMPOSSIBLE'

def main():
    r, c = map(int, input().split())
    maze = ['@'*(c+2)] + ['@'+input().rstrip()+'@' for _ in range(r)] + ['@'*(c+2)]
    r += 2 ; c += 2
    jihoon, fires = (0, 0), []
    for i, line in enumerate(maze):
        if 'J' in line:
            jihoon = (i, line.find('J'))
        for j, x in enumerate(line):
            if x == 'F':
                fires.append((i, j))
    fired = [[-1]*c for _ in range(r)]
    fire_route(maze, fired, fires)
    print(escape_route(maze, fired, jihoon))

if __name__ == "__main__":
    main()