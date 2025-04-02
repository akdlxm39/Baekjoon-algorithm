import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2-x1*y3 + x2*y3-x2*y1 + x3*y1-x3*y2

def check(x1, y1, x2, y2, x3, y3, x4, y4):
    if ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4) < 0:
        if ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2) < 0:
            return True
    return False

def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    print(1 if check(x1, y1, x2, y2, x3, y3, x4, y4) else 0)

if __name__ == "__main__":
    main()