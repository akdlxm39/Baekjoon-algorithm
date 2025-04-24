import sys
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = sorted(tuple(map(int, input().split())) for _ in range(n))
        point_set = set(points)
        ans = 0
        for i in range(n-1):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if y1 >= y2:
                    continue
                dx, dy = x2 - x1, y2 - y1
                size = dx*dx+dy*dy
                if ans < size and (x1+dy, y1-dx) in point_set and (x2+dy, y2-dx) in point_set:
                    ans = size
        print(ans)

if __name__ == "__main__":
    main()