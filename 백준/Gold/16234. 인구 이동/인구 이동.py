import sys
input = sys.stdin.readline

def union_move(n, l, r, countries, visited, i, j, day):
    union = [(i, j)]
    visited[i][j] = day
    union_idx = 0
    union_len = 1
    population = 0
    while union_idx < union_len:
        x, y = union[union_idx]
        population += countries[x][y]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]==day:
                continue
            if not (l <= abs(countries[x][y] - countries[nx][ny]) <= r):
                continue
            visited[nx][ny] = day
            union.append((nx, ny))
            union_len += 1
        union_idx += 1
    if union_len > 1:
        population //= union_idx
        for x, y in union:
            countries[x][y] = population
        return union
    return []

def day_of_moves(n, l, r, countries):
    day = -1
    queue = [(i, j) for i in range(n) for j in range(i%2, n, 2)]
    visited = [[-1] * n for _ in range(n)]
    while queue:
        day += 1
        nxt_queue = []
        for i, j in queue:
            if visited[i][j] == day:
                continue
            nxt_queue += union_move(n, l, r, countries, visited, i, j, day)
        queue = nxt_queue
    return day

def main():
    n, l, r = map(int, input().split())
    countries = [list(map(int, input().split())) for _ in range(n)]
    print(day_of_moves(n, l, r, countries))

if __name__ == "__main__":
    main()