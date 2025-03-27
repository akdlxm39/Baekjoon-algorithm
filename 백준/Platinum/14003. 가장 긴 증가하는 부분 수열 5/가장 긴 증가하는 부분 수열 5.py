import sys
input = sys.stdin.readline

def lower_bound(arr, target):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return l

def main():
    n = int(input())
    num_list = list(map(int, input().split()))
    stack = []
    dp = [0] * n
    for i, num in enumerate(num_list):
        if not stack or stack[-1] < num:
            stack.append(num)
            dp[i] = len(stack)
        else:
            index = lower_bound(stack, num)
            stack[index] = num
            dp[i] = index+1
    cnt = len(stack)
    ans = [0]*cnt
    while cnt and n:
        n -= 1
        if dp[n] == cnt:
            cnt -= 1
            ans[cnt] = num_list[n]
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    main()