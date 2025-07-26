import sys
from itertools import combinations

input = sys.stdin.readline
INF = 10000
dx, dy = [0, 0, 1, -1], [-1, 1, 0, 0]

def bfs(n, room, virus, need, min_time):
    queue = list(virus)
    visited = [[False] * n for _ in range(n)]
    for x, y in queue: visited[x][y] = True
    for times in range(1, min_time):
        nxt_queue = []
        for cx, cy in queue:
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if not (0<=nx<n and 0<=ny<n) or visited[nx][ny] or room[nx][ny] == 1: continue
                if room[nx][ny] == 0:
                    need -= 1
                    if need == 0:
                        return times
                visited[nx][ny] = True
                nxt_queue.append((nx, ny))
        queue = nxt_queue

    return INF

def main():
    n, m = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    virus = []
    need = 0
    for i in range(n):
        for j in range(n):
            if room[i][j] == 2:
                virus.append((i, j))
            elif room[i][j] == 0:
                need += 1
    if need == 0:
        print(0)
    else:
        min_time = INF
        for cur_virus in combinations(virus, m):
            min_time = min(min_time, bfs(n, room, cur_virus, need, min_time))
        print(min_time if min_time != INF else -1)

if __name__ == "__main__":
    main()
