import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def main():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    ans = 0
    for i in range(n):
        point_dxdy_dict = dict()
        x1, y1 = points[i]
        for j in range(n):
            if i == j: continue
            x2, y2 = points[j]
            if x1==x2: dx, dy = 0, 1
            elif y1==y2: dx, dy = 1, 0
            elif x1<x2: dx, dy = x2-x1, y2-y1
            else: dx, dy = x1-x2, y1-y2
            g = gcd(abs(dx), abs(dy))
            dx //= g ; dy //= g
            point_dxdy_dict.setdefault((dx, dy), 0)
            point_dxdy_dict[(dx, dy)] += 1
        for (dx, dy), cnt in point_dxdy_dict.items():
            if dy >= 0 and (dy, -dx) in point_dxdy_dict:
                ans += cnt * point_dxdy_dict[(dy, -dx)]
            elif (-dy, dx) in point_dxdy_dict:
                ans += cnt * point_dxdy_dict[(-dy, dx)]
    print(ans//2)

if __name__ == "__main__":
    main()