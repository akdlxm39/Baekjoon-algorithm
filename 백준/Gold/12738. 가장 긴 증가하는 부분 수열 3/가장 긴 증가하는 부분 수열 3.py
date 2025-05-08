import sys
from bisect import bisect_left
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    ans_list = [nums[0]]
    ans = 1
    for i in range(1, n):
        if ans_list[-1] < nums[i]:
            ans_list.append(nums[i])
            ans += 1
        else:
            ans_list[bisect_left(ans_list, nums[i])] = nums[i]
    print(ans)


if __name__ == "__main__":
    main()