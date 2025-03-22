import sys
from functools import cmp_to_key
input = sys.stdin.readline

def comp(a, b):
    if len(a) == len(b):
        return 1 if a < b else -1
    return 1 if a+b < b+a else -1

def main():
    n = int(input())
    nums = list(input().split())
    nums.sort(key=cmp_to_key(comp))
    print(''.join(nums) if nums[0]!='0' else 0)

if __name__ == "__main__":
    main()