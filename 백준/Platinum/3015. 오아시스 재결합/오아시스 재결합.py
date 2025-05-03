import sys
input = sys.stdin.readline

def upper_bound(stack, x):
    l, r = 0, len(stack)
    while l < r:
        mid = (l+r)//2
        if x <= stack[mid]:
            l = mid+1
        else:
            r = mid
    return l

def main():
    n = int(input())
    stack = [int(input())]
    ans = 0
    for _ in range(n-1):
        x = int(input())
        ans += len(stack)
        del stack[upper_bound(stack, x):]
        if stack and stack[0] > x:
            ans -= upper_bound(stack, x+1)-1
        stack.append(x)
    print(ans)

if __name__ == "__main__":
    main()