from collections import deque


class Point:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __add__(self, other):
        return Point(self.y + other.y, self.x + other.x)

    def is_valid(self, n, map_, dist):
        return (
            0 <= self.y < n
            and 0 <= self.x < n
            and map_[self.y][self.x] != "1"
            and dist[self.y][self.x] == -1
        )


DIR = (Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1))


def solve():
    n: int = int(input())
    map_: list[str] = [input() for _ in range(n)]
    dist: list[list[int]] = [[-1] * n for _ in range(n)]
    queue: deque[Point] = deque()
    for i, s in enumerate(map_):
        j = s.find("2")
        if j != -1:
            queue.append(Point(i, j))
            dist[i][j] = 0
            break
    while queue:
        cur = queue.popleft()
        for d in DIR:
            nxt = cur + d
            if not nxt.is_valid(n, map_, dist):
                continue
            if map_[nxt.y][nxt.x] == "3":
                return dist[cur.y][cur.x]
            dist[nxt.y][nxt.x] = dist[cur.y][cur.x] + 1
            queue.append(nxt)
    return 0


for test_case in range(1, int(input()) + 1):
    print(f"#{test_case} {solve()}")
