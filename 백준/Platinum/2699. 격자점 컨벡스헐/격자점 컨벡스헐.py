import sys
from functools import cmp_to_key
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    c = (x2-x1)*(y3-y2) - (x3-x2)*(y2-y1)
    return c

def distance(x1, y1, x2, y2):
    return (x2-x1)**2 + (y2-y1)**2

def main():
    p = int(input())
    for _ in range(p):
        n = int(input())
        points = []
        for _ in range((n-1)//5+1):
            nums = tuple(map(int, input().split()))
            points += [(nums[i],nums[i+1]) for i in range(0, len(nums), 2)]
        start = max(points, key=lambda p: (p[1],-p[0]))
        def ccw_cmp(p1, p2):
            c = ccw(start[0], start[1], p1[0], p1[1], p2[0], p2[1])
            if c == 0:
                return 1 if distance(start[0], start[1], p1[0], p1[1]) > distance(start[0], start[1], p2[0], p2[1]) else -1
            return 1 if c>0 else -1
        points.sort(key=cmp_to_key(ccw_cmp))
        ans = points[:2]
        for point in points[2:]:
            while len(ans)>=2 and ccw(*ans[-2], *ans[-1], *point) >= 0:
                ans.pop()
            ans.append(point)
        print(len(ans), '\n'.join(map(lambda x: ' '.join(map(str, x)), ans)), sep='\n')

if __name__ == "__main__":
    main()