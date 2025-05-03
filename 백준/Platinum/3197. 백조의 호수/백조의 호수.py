import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline

def lake_init(r, c, lake, visited, i, j, init_queue):
    visited[i][j] = 0
    queue = deque([(i,j)])
    while queue:
        x, y = queue.popleft()
        flag = False
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == -1:
                if lake[nx][ny] == 'X': flag = True; continue
                visited[nx][ny] = 0
                queue.append((nx, ny))
        if flag: init_queue.append((x, y))

def melt(r, c, visited, date, cur_queue):
    nxt_queue = []
    for x, y in cur_queue:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0<=nx<r and 0<=ny<c:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = date
                    nxt_queue.append((nx, ny))
    return nxt_queue

def find_route(r, c, lake, swan):
    max_date = 0
    visited = [[False]*c for _ in range(r)]
    heap = [(0, swan[0][0], swan[0][1])]
    while heap:
        date, x, y = heappop(heap)
        max_date = max(max_date, date)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not (0<=nx<r and 0<=ny<c) or visited[nx][ny]: continue
            if nx==swan[1][0] and ny==swan[1][1]:
                return max_date
            visited[nx][ny] = True
            heappush(heap, (lake[nx][ny], nx, ny))

def main():
    r, c = map(int, input().split())
    lake = [input().rstrip() for _ in range(r)]
    swan = []
    visited = [[-1]*c for _ in range(r)]
    queue = []
    for i in range(r):
        for j in range(c):
            if lake[i][j] == 'L': swan.append((i, j))
            if lake[i][j]=='X' or visited[i][j]==0: continue
            lake_init(r, c, lake, visited, i, j, queue)
    date = 1
    while queue:
        queue = melt(r, c, visited, date, queue)
        date += 1
    print(find_route(r, c, visited, swan))


if __name__ == "__main__":
    main()