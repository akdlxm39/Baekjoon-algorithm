import sys
input = sys.stdin.readline

def ccw(v1, v2):
    c = v1[0] * v2[1] - v2[0] * v1[1]
    if c == 0:
        return 0
    return 1 if c>0 else -1

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    v1 = (x2 - x1), (y2 - y1)
    v2 = (x3 - x2), (y3 - y2)
    print(ccw(v1, v2))

if __name__ == "__main__":
    main()