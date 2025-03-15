import sys
input = sys.stdin.readline

def main():
    price, a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    acnt = price//a+1
    ans = cur = a * acnt
    memo = {cur:True}
    while acnt:
        nxt = cur - a
        tmp = price - nxt
        cur = nxt + (tmp//b+(tmp%b!=0))*b
        ans = min(ans, cur)
        if cur in memo:
            break
        else:
            memo[cur] = True
        acnt -= 1
    print(ans)

if __name__ == "__main__":
    main()