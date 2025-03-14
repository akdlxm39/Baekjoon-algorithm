import sys
input = sys.stdin.readline

def main():
    t = int(input())
    l, r = map(int, input().split())
    ans = int(l and l==r)
    for _ in range(t-1):
        (prev_l, prev_r), (l, r) = (l, r), map(int, input().split())
        ans += (l and l==prev_l) + (r and r==prev_r) + (l and l==r)
    print(ans)

if __name__ == "__main__":
    main()