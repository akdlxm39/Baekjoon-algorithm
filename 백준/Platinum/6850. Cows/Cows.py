import sys
import math
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)
    return c

def convexhull(points):
    points.sort()
    st1 = []
    st2 = []
    for point in points:
        while len(st1) >= 2 and ccw(*st1[-2], *st1[-1], *point) >= 0: st1.pop()
        while len(st2) >= 2 and ccw(*st2[-2], *st2[-1], *point) <= 0: st2.pop()
        st1.append(point)
        st2.append(point)
    return st1 + st2[-2:0:-1]

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def triangleS(x1, y1, x2, y2, x3, y3):
    l1 = distance(x1, y1, x2, y2)
    l2 = distance(x1, y1, x3, y3)
    l3 = distance(x2, y2, x3, y3)
    theta = math.acos((l1*l1+l2*l2-l3*l3)/(2*l1*l2))
    return l1*l2*math.sin(theta)/2

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    convex = convexhull(points)
    ans = 0
    for i in range(1, len(convex)-1):
        ans += triangleS(*convex[0], *convex[i], *convex[i+1])
    print(int(ans//50))

if __name__ == "__main__":
    main()