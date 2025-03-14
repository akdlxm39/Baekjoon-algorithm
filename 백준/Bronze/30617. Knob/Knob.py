import sys
input = sys.stdin.readline

def main():
    t = int(input())
    prev_l, prev_r = map(int, input().split())
    ans = int(prev_l and prev_l==prev_r)
    for _ in range(t-1):
        l, r = map(int, input().split())
        if l==prev_l:
            ans += l!=0
        else:
            prev_l = l
        if prev_r == r:
            ans += r!=0
        else:
            prev_r = r
        if l==r:
            ans += l!=0
    print(ans)

if __name__ == "__main__":
    main()