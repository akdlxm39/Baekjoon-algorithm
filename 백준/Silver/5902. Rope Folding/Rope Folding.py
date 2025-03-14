import sys
input = sys.stdin.readline

def main():
    n, l = map(int, input().split())
    knots = sorted(int(input()) for _ in range(n))
    gaps = [b-a for a, b in zip(knots, knots[1:])]
    rgaps = gaps[::-1]
    ans = 0
    for i in range(1, 2*(n-1)):
        g1, g2 = max(0, i-n+1), min(i, n-1)
        r1, r2 = n-1-g2, n-1-g1
        if gaps[g1:g2] == rgaps[r1:r2]:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()