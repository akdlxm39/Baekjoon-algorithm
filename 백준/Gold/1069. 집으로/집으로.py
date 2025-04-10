import sys
input = sys.stdin.readline

def main():
    x, y, d, t = map(int, input().split())
    l = (x*x+y*y)**0.5
    n = l//d
    if n:
        a = l%d
        ans = min(n*t+a, (n+1)*t, l)
    else:
        ans = min(t+d-l, l, 2*t)
    print(ans)

if __name__ == "__main__":
    main()