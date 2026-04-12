from collections import deque

n = 0
ans = 0
map_ = []
dist_ = []


class Point:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __add__(self, other):
        return Point(self.y + other.y, self.x + other.x)

    def is_valid(self):
        return (
            0 <= self.y < n
            and 0 <= self.x < n
            and map_[self.y][self.x] != "1"
            and dist_[self.y][self.x] == -1
        )

    def map_val(self):
        return map_[self.y][self.x]

    def get_dist(self):
        return dist_[self.y][self.x]

    def set_dist(self, val):
        dist_[self.y][self.x] = val


start: Point = Point(-1, -1)


# 방향 벡터
DIR = [Point(-1, 0), Point(1, 0), Point(0, -1), Point(0, 1)]


def bfs():
    q: deque[Point] = deque([start])
    start.set_dist(0)
    while q:
        cur = q.popleft()
        for d in DIR:
            nxt = cur + d
            if not nxt.is_valid():
                continue
            if nxt.map_val() == "3":
                return cur.get_dist()
            nxt.set_dist(cur.get_dist() + 1)
            q.append(nxt)
    return 0


def input_data():
    global n, map_, dist_, start
    n = int(input())
    map_ = []
    dist_ = []
    for i in range(n):
        row = input()
        map_.append(row)
        dist_.append([-1] * n)
        if "2" in row:
            start = Point(i, row.index("2"))


def solve():
    global ans
    ans = bfs()


def output(test_case):
    print(f"#{test_case} {ans}")


def main():
    for test_case in range(1, int(input()) + 1):
        input_data()
        solve()
        output(test_case)


if __name__ == "__main__":
    main()
