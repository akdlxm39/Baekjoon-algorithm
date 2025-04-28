import sys
from collections import deque
input = sys.stdin.readline

def union_move(n, l, r, countries, visited, i, j):
    queue = deque([(i, j)])
    union = []
    union_cnt = 0
    population = 0
    while queue:
        x, y = queue.popleft()
        union.append((x, y))
        union_cnt += 1
        population += countries[x][y]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]:
                continue
            if not (l <= abs(countries[x][y] - countries[nx][ny]) <= r):
                continue
            visited[nx][ny] = True
            queue.append((nx, ny))
    if union_cnt == 1:
        return False
    population //= union_cnt
    for x, y in union:
        countries[x][y] = population
    return True

def day(n, l, r, countries):
    visited = [[False] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            visited[i][j] = True
            if union_move(n, l, r, countries, visited, i, j):
                flag = True
    return flag

def main():
    n, l, r = map(int, input().split())
    countries = [list(map(int, input().split())) for _ in range(n)]
    day_cnt = 0
    while day(n, l, r, countries):
        day_cnt += 1
    print(day_cnt)

if __name__ == "__main__":
    main()