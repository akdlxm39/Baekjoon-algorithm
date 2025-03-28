import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    stack = []
    for i in range(n-1, -1, -1):
        num = nums[i]
        while stack:
            if num < stack[-1]:
                nums[i] = stack[-1]
                break
            stack.pop()
        else:
            nums[i] = -1
        stack.append(num)
    print(*nums)

if __name__ == "__main__":
    main()