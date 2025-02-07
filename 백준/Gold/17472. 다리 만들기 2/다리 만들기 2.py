import sys
from heapq import heapify, heappush, heappop
from collections import deque
from itertools import product
input = sys.stdin.readline

def island(n, m, maps, heap, x, y):
    queue = deque([(x, y)])
    maps[x][y] = 2
    land = 1
    while queue:
        cx, cy = queue.popleft()
        delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < n and 0 <= ny < m) or maps[nx][ny] == 2:
                continue
            if maps[nx][ny] == 0:
                heappush(heap, (1, nx, ny, dx, dy))
            elif maps[nx][ny] == 1:
                queue.append((nx, ny))
                maps[nx][ny] = 2
                land += 1
    return land

def main():
    n, m = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(n)]
    land = sum(sum(m) for m in maps)
    heap = []
    ans = 0
    for i, j in product(range(n), range(m)):
        if maps[i][j] == 1:
            land -= island(n, m, maps, heap, i, j)
            break
    while land:
        if not heap:
            ans = -1
            break
        dist, cx, cy, dx, dy = heappop(heap)
        nx, ny = cx + dx, cy + dy
        if not (0 <= nx < n and 0 <= ny < m) or maps[nx][ny] == 2:
            continue
        elif maps[nx][ny] == 0:
            heappush(heap, (dist + 1, nx, ny, dx, dy))
        elif maps[nx][ny] == 1 and dist >= 2:
            ans += dist
            land -= island(n, m, maps, heap, nx, ny)
    print(ans)

if __name__ == "__main__":
    main()