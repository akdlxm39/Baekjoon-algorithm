import sys
input = sys.stdin.readline

def main():
    price, a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    acnt, bcnt = (price-1)//a+1, 0
    ans = cur = a * acnt
    memo = {cur}
    while acnt:
        acnt -= 1
        if acnt*a +bcnt*b < price:
            bcnt = (price - acnt*a - 1) // b + 1
        cur = acnt*a +bcnt*b
        if cur in memo:
            break
        memo.add(cur)
        ans = min(ans, cur)
    print(ans)

if __name__ == "__main__":
    main()