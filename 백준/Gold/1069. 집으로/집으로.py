import sys
input = sys.stdin.readline

def main():
    x, y, d, t = map(int, input().split())
    l = (x*x+y*y)**0.5
    n = l//d
    ans = min(n*t+l%d, (n+1)*t, l) if n else min(t+d-l, 2*t, l)
    print(ans)

if __name__ == "__main__":
    main()