import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    n = int(input())
    num_list = input().split()
    stack = []
    dp = [0] * n
    for i in range(n):
        num = int(num_list[i])
        if not stack or stack[-1] < num:
            stack.append(num)
            dp[i] = len(stack)
        else:
            index = bisect_left(stack, num)
            stack[index] = num
            dp[i] = index+1
    cnt = len(stack)
    ans = [""]*cnt
    for i in range(n-1,-1,-1):
        if dp[i] == cnt:
            cnt -= 1
            ans[cnt] = num_list[i]
    print(len(ans))
    print(' '.join(ans))

if __name__ == "__main__":
    main()