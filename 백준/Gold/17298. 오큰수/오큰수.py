import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    stack = []
    ans = [-1]*n
    for i in range(n-1, -1, -1):
        while stack:
            if nums[i] < stack[-1]:
                ans[i] = stack[-1]
                break
            stack.pop()
        stack.append(nums[i])
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()