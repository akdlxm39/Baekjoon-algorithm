import sys
input = sys.stdin.readline

def ccw(x1,y1,x2,y2,x3,y3):
    c = (x2-x1)*(y3-y2)-(x3-x2)*(y2-y1)
    return 0 if c==0 else 1 if c>0 else -1

def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    c1 = ccw(x1,y1,x2,y2,x3,y3)
    c2 = ccw(x1,y1,x2,y2,x4,y4)
    c3 = ccw(x3,y3,x4,y4,x1,y1)
    c4 = ccw(x3,y3,x4,y4,x2,y2)
    if c1 == 0 and c2 == 0 and c3 == 0 and c4 == 0:
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2):
            if min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
                return True
    elif c1 * c2 <= 0 and c3 * c4 <= 0:
        return True
    return False

def main():
    t = int(input())
    for _ in range(t):
        x, y = [0,0], [0,0]
        x1, y1, x2, y2, x[0], y[0], x[1], y[1] = map(int, input().split())
        x.sort()
        y.sort()
        if x[0]<=x1<=x[1] and x[0]<=x2<=x[1] and y[0]<=y1<=y[1] and y[0]<=y2<=y[1]:
            print('T')
            continue
        for i in range(2):
            if is_cross(x1,y1,x2,y2,x[i],y[0],x[i],y[1]) or is_cross(x1,y1,x2,y2,x[0],y[i],x[1],y[i]):
                print('T')
                break
        else:
            print('F')

if __name__ == "__main__":
    main()