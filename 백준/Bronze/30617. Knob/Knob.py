import sys
input = sys.stdin.readline

def main():
    t = int(input())
    prev_l, prev_r = map(int, input().split())
    ans = int(prev_l and prev_r and prev_l==prev_r)
    for _ in range(t-1):
        l, r = map(int, input().split())
        if l:
            ans += l==prev_l
        if r:
            ans += r==prev_r
        if l and r:
            ans += l==r
        prev_l, prev_r = l, r
    print(ans)

if __name__ == "__main__":
    main()