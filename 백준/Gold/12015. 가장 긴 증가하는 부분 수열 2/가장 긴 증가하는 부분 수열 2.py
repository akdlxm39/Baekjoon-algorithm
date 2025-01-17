import sys
input = sys.stdin.readline
from bisect import bisect_left

def main():
    N = int(input())
    nums = list(map(int, input().split()))
    dp = [nums[0]]
    for num in nums[1:]:
        if dp[-1] < num:
            dp.append(num)
        else:
            dp[bisect_left(dp, num)] = num
    print(len(dp))
    
main()