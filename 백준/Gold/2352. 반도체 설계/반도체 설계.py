import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    _ = int(input())
    stack = [0]
    for num in map(int, input().split()):
        if num > stack[-1]:
            stack.append(num)
        else:
            stack[bisect_left(stack, num)] = num
    print(len(stack) - 1)

if __name__ == "__main__":
    main()