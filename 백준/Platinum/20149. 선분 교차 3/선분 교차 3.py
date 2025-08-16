import sys

input = sys.stdin.readline


def dist(x1, y1, x2, y2):
    return ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5


def ccw(x1, y1, x2, y2, x3, y3):
    res = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0


def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)
    ccw3 = ccw(x3, y3, x4, y4, x1, y1)
    ccw4 = ccw(x3, y3, x4, y4, x2, y2)
    if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
        length_sum = dist(x1, y1, x2, y2) + dist(x3, y3, x4, y4)
        max_dist = max(dist(x1, y1, x3, y3), dist(x1, y1, x4, y4),
                       dist(x2, y2, x3, y3), dist(x2, y2, x4, y4))
        gap = max_dist - length_sum
        if gap > 0:
            print(0)
        elif gap < 0:
            print(1)
        else:
            print(1)
            if (x1 == x3 and y1 == y3) or (x1 == x4 and y1 == y4):
                print(x1, y1)
            else:
                print(x2, y2)
    else:
        cross1 = ccw1 * ccw2
        cross2 = ccw3 * ccw4
        if cross1 == 1 or cross2 == 1:
            print(0)
        elif cross1 == 0 or cross2 == 0:
            print(1)
            if ccw1 == 0:
                print(x3, y3)
            elif ccw2 == 0:
                print(x4, y4)
            elif ccw3 == 0:
                print(x1, y1)
            elif ccw4 == 0:
                print(x2, y2)
        elif cross1 == -1 and cross2 == -1:
            print(1)
            a = (y2 - y1) / (x2 - x1) if x1 != x2 else None
            b = y1 - a * x1 if a is not None else None
            c = (y4 - y3) / (x4 - x3) if x3 != x4 else None
            d = y3 - c * x3 if c is not None else None
            if a is None:
                print(x1, c * x1 + d)
            elif c is None:
                print(x3, a * x3 + b)
            else:
                x = (d - b) / (a - c)
                print(x, a * x + b)


if __name__ == "__main__":
    main()
