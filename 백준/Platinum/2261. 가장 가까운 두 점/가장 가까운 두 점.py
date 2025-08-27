import sys

input = sys.stdin.readline
INF = int(1e9)


def dist(p1, p2):
    return (p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1])


def divide_and_conquer(points, left, right):
    if left == right:
        return INF
    elif right - left == 1:
        return dist(points[left], points[right])
    mid = (left + right) // 2
    res = min(divide_and_conquer(points, left, mid), divide_and_conquer(points, mid + 1, right))

    candidate = []
    for i in range(left, right + 1):
        dx = points[i][0] - points[mid][0]
        if dx * dx < res:
            candidate.append(points[i])
    candidate.sort(key=lambda p: p[1])
    for i in range(len(candidate) - 1):
        for j in range(i + 1, len(candidate)):
            dy = candidate[j][1] - candidate[i][1]
            if dy * dy >= res:
                break
            res = min(res, dist(candidate[i], candidate[j]))
    return res


def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    points.sort()
    print(divide_and_conquer(points, 0, n - 1))


if __name__ == "__main__":
    main()
