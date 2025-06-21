import sys
input = sys.stdin.readline
INF = int(1e11)

def solve(nums, x, start, end):
    gap = INF
    ans = -1
    left, right = start, end
    while left <= right:
        mid = (left + right) // 2
        cur_gap = x+nums[mid]
        if cur_gap == 0:
            return 0, nums[mid]
        if abs(cur_gap) < gap:
            gap = abs(cur_gap)
            ans = nums[mid]
        if cur_gap < 0:
            left = mid + 1
        else:
            right = mid-1
    return gap, ans

def main():
    n = int(input())
    nums = sorted(map(int, input().split()))
    gap = INF
    ans = (-1, -1)
    for i in range(n-1):
        cur_gap, cur_ans = solve(nums, nums[i], i+1, n-1)
        if cur_gap < gap:
            gap = cur_gap
            ans = (nums[i], cur_ans)
    print(*ans)

if __name__ == "__main__":
    main()