import sys

input = sys.stdin.readline
INF = int(1e9)

def extended_euclid(a, b):
    x1, y1, r1 = 1, 0, a
    x2, y2, r2 = 0, 1, b
    while r2 != 0:
        q = r1 // r2
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
        r1, r2 = r2, r1 - q * r2
    return x1, y1, r1


def main():
    t = int(input())
    for _ in range(t):
        k, c = map(int, input().split())
        if c == 1:
            print(k+1 if k < INF else "IMPOSSIBLE")
            continue
        if k == 1:
            print(1)
            continue
        x1, y1, r1 = extended_euclid(k, c)
        if r1 != 1 or y1 > INF:
            print("IMPOSSIBLE")
        else:
            while y1 < 0:
                y1 += k
            print(y1)


if __name__ == "__main__":
    main()
