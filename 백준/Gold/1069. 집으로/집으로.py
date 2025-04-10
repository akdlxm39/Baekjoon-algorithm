import sys
input = sys.stdin.readline

def main():
    x, y, d, t = map(int, input().split())
    l = (x*x+y*y)**0.5
    ans = min(l//d*t+l%d, (l//d+1)*t, l) if l>d else min(t+d-l, 2*t, l)
    print(ans)

if __name__ == "__main__":
    main()