import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = sorted(int(input()) for _ in range(n))
    xy_set = set(nums)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            xy_set.add(nums[i]+nums[j])
    for i in range(n):
        for j in range(i+1):
            if nums[i]-nums[j] in xy_set:
                ans = nums[i]
    print(ans)

if __name__ == "__main__":
    main()