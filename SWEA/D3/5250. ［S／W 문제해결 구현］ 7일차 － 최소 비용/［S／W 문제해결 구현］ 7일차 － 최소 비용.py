from heapq import heappop, heappush

INF = int(1e10)
DIR = ((-1, 0), (1, 0), (0, -1), (0, 1))


def solve():
    n = int(input())
    map_ = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    heap = [(0, 0, 0)]
    dist[0][0] = 0
    while heap:
        d, y, x = heappop(heap)
        if y == n - 1 and x == n - 1:
            return d
        if dist[y][x] < d:
            continue
        for dy, dx in DIR:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < n and 0 <= nx < n):
                continue
            nd = d + 1 + max(0, map_[ny][nx] - map_[y][x])
            if dist[ny][nx] <= nd:
                continue
            dist[ny][nx] = nd
            heappush(heap, (nd, ny, nx))
    return dist[n - 1][n - 1]


def main():
    for test_case in range(1, int(input()) + 1):
        print(f"#{test_case} {solve()}")


if __name__ == "__main__":
    main()
