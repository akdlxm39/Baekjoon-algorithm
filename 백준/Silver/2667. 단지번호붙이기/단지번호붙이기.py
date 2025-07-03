import sys
input = sys.stdin.readline
dxdy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(n, map_, visited, x, y):
    queue = [(x, y)]
    visited[x][y] = True
    res = 1
    while queue:
        nxt_queue = []
        for cx, cy in queue:
            for dx, dy in dxdy:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < n and 0 <= ny < n) or map_[nx][ny]=='0' or visited[nx][ny]: continue
                visited[nx][ny] = True
                nxt_queue.append((nx, ny))
                res += 1
        queue = nxt_queue
    return res

def main():
    n = int(input())
    map_ = [input().rstrip() for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    ans = []
    for i in range(n):
        for j in range(n):
            if map_[i][j] == '0' or visited[i][j]: continue
            ans.append(bfs(n, map_, visited, i, j))
    print(len(ans), *sorted(ans), sep='\n')

if __name__ == "__main__":
    main()