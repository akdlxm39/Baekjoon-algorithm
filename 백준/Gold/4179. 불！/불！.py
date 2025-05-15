import sys
from collections import deque
input = sys.stdin.readline

def escape(r, c, maze, jihoon, fires):
    visited = [[False]*c for _ in range(r)]
    visited[jihoon[0]][jihoon[1]] = True
    for fx, fy in fires:
        visited[fx][fy] = True
    fire_queue = fires
    j_queue = [jihoon]
    date = 1
    while j_queue:
        next_fire_queue = []
        for fx, fy in fire_queue:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nfx, nfy = fx + dx, fy + dy
                if visited[nfx][nfy] or maze[nfx][nfy]=='#' or maze[nfx][nfy]=='@':
                    continue
                visited[nfx][nfy] = True
                next_fire_queue.append((nfx, nfy))
        fire_queue = next_fire_queue
        next_j_queue = []
        for jx, jy in j_queue:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                njx, njy = jx + dx, jy + dy
                if maze[njx][njy] == '@':
                    return date
                if visited[njx][njy] or maze[njx][njy] == '#':
                    continue
                visited[njx][njy] = True
                next_j_queue.append((njx, njy))
        j_queue = next_j_queue
        date += 1
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
    print(escape(r, c, maze, jihoon, fires))

if __name__ == "__main__":
    main()