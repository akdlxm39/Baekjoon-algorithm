import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(input().split())
    nums.sort(key = lambda x: x*9, reverse=True)
    print(''.join(nums) if nums[0]!='0' else 0)

if __name__ == "__main__":
    main()