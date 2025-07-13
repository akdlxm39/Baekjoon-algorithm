import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    stack = []
    for num in nums:
        if not stack or num > stack[-1]:
            stack.append(num)
        else:
            stack[bisect_left(stack, num)] = num
    print(len(stack))

if __name__ == "__main__":
    main()