import sys
input = sys.stdin.readline
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(n, m, map_, x, y):
    queue = [(x, y)]
    while queue:
        nxt_queue = []
        for cx, cy in queue:
            for dx, dy in dxdy:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < n and 0 <= ny < m) or map_[nx][ny]==0: continue
                map_[nx][ny] = 0
                nxt_queue.append((nx, ny))
        queue = nxt_queue

def main():
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        map_ = [[False]*m for _ in range(n)]
        for _ in range(k):
            x, y = map(int, input().split())
            map_[y][x] = True
        ans = 0
        for i in range(n):
            for j in range(m):
                if map_[i][j] == 0: continue
                bfs(n, m, map_, i, j)
                ans += 1
        print(ans)

if __name__ == "__main__":
    main()