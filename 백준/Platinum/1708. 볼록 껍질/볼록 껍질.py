import sys
from functools import cmp_to_key
input = sys.stdin.readline

def ccw(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p2[1]) - (p3[0] - p2[0]) * (p2[1] - p1[1])

def dist(p1, p2):
    return (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    start_point = min(points)
    def cmp(p2, p3, p1=start_point):
        c = ccw(p1, p2, p3)
        if c==0:
            return 1 if dist(p1, p2) > dist(p1, p3) else -1
        return -1 if c > 0 else 1
    points.sort(key=cmp_to_key(cmp))
    stack = [points[0], points[1]]
    for i in range(2, n):
        while len(stack) >= 2:
            c = ccw(stack[-2], stack[-1], points[i])
            if c > 0:
                stack.append(points[i])
                break
            elif c < 0:
                stack.pop()
            else:
                if dist(stack[-2], stack[-1]) < dist(stack[-2], points[i]):
                    stack.pop()
                    stack.append(points[i])
                break
    print(len(stack))

if __name__ == "__main__":
    main()