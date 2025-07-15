import sys
input = sys.stdin.readline
dx, dy = [0,0,1,-1], [1,-1,0,0]

def find(n, map_, x, y, size):
    queue = [(x, y)]
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    nearest_fishes = []
    dist = 0
    while queue:
        dist += 1
        nxt_queue = []
        for cx, cy in queue:
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]: continue
                visited[nx][ny] = True
                if map_[nx][ny] > size: continue
                nxt_queue.append((nx, ny))
                if 0 < map_[nx][ny] < size:
                    nearest_fishes.append((nx, ny))
        if nearest_fishes:
            return min(nearest_fishes), dist
        queue = nxt_queue
    return (-1, -1), -1

def main():
    n = int(input())
    map_ = [list(map(int, input().split())) for _ in range(n)]
    x, y = 0, 0
    for i in range(n):
        if 9 in map_[i]:
            x, y = i, map_[i].index(9)
            break
    map_[x][y] = 0
    size = 2
    feed = time = 0
    while True:
        (x, y), dist = find(n, map_, x, y, size)
        if x == -1: break
        map_[x][y] = 0
        feed += 1
        if feed == size:
            size += 1
            feed = 0
        time += dist
    print(time)

if __name__ == "__main__":
    main()