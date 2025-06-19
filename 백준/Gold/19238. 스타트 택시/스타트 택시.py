import sys
from collections import deque
input = sys.stdin.readline
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def pickup(n, map_, oil, x, y):
    if map_[x][y] > 1: return x, y, oil
    visited = [[False]*n for _ in range(n)]
    queue = [(x, y)]
    visited[x][y] = True
    for dist in range(oil):
        customers = []
        nxt_queue = []
        for cx, cy in queue:
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny] or map_[nx][ny] == 1: continue
                if map_[nx][ny] > 1: customers.append((nx, ny))
                visited[nx][ny] = True
                nxt_queue.append((nx, ny))
        if customers:
            cx, cy = min(customers)
            return cx, cy, oil-dist-1
        queue = nxt_queue
    return -1, -1, -1

def move(n, map_, oil, x, y, ax, ay):
    visited = [[False]*n for _ in range(n)]
    queue = deque([(x, y, 0)])
    visited[x][y] = True
    while queue:
        cx, cy, dist = queue.popleft()
        if dist > oil: break
        if cx == ax and cy == ay: return oil+dist
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny] or map_[nx][ny] == 1: continue
            visited[nx][ny] = True
            queue.append((nx, ny, dist + 1))
    return -1

def main():
    n, m, oil = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(n)]
    x, y = map(lambda a:int(a)-1, input().split())
    destinations = [(0, 0)]*(m+2)
    for i in range(2, m+2):
        sx, sy, ex, ey = map(lambda a:int(a)-1, input().split())
        map_[sx][sy] = i
        destinations[i] = (ex, ey)
    for _ in range(m):
        cx, cy, oil = pickup(n, map_, oil, x, y)
        if oil == -1: break
        dx, dy = destinations[map_[cx][cy]]
        map_[cx][cy] = 0
        oil = move(n, map_, oil, cx, cy, dx, dy)
        if oil == -1: break
        x, y = dx, dy
    print(oil)

if __name__ == "__main__":
    main()