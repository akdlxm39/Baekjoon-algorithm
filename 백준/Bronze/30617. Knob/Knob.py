import sys
input = sys.stdin.readline

def main():
    t = int(input())
    prev_l, prev_r = map(int, input().split())
    ans = int(prev_l and prev_r and prev_l==prev_r)
    for _ in range(t-1):
        l, r = map(int, input().split())
        ans += (l and l==prev_l) + (r and r==prev_r) + (l and l==r)
        prev_l, prev_r = l, r
    print(ans)

if __name__ == "__main__":
    main()