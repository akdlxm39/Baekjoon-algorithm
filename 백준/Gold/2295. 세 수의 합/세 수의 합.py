import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

def main():
    n = int(input())
    nums = sorted(int(input()) for _ in range(n))
    xy_set = {x+y for x, y in combinations_with_replacement(nums, 2)}
    for i in range(n-1, 0, -1):
        for j in range(i):
            if nums[i]-nums[j] in xy_set:
                print(nums[i])
                return

if __name__ == "__main__":
    main()