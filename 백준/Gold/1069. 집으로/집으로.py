import sys
input = sys.stdin.readline

def main():
    x, y, d, t = map(int, input().split())
    l = (x*x+y*y)**0.5
    n = l//d
    if n:
        ans = n*t + min(l%d, t)
    else:
        ans = t + min(d-l, t)
    print(min(ans, l))

if __name__ == "__main__":
    main()