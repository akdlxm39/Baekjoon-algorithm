import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    c = x1*y2-x1*y3 + x2*y3-x2*y1 + x3*y1-x3*y2
    return 0 if c==0 else 1 if c>0 else -1

def check(x1, y1, x2, y2, x3, y3, x4, y4):
    c1 = ccw(x1, y1, x2, y2, x3, y3)
    c2 = ccw(x1, y1, x2, y2, x4, y4)
    c3 = ccw(x3, y3, x4, y4, x1, y1)
    c4 = ccw(x3, y3, x4, y4, x2, y2)
    if c1==0 and c2==0 and c3==0 and c4==0:
        if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2):
            if min(y1,y2)<=max(y3,y4) and min(y3,y4)<=max(y1,y2):
                return True
    elif c1*c2 <= 0 and c3*c4 <= 0:
            return True
    return False

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    print(1 if check(x1, y1, x2, y2, x3, y3, x4, y4) else 0)

if __name__ == "__main__":
    main()