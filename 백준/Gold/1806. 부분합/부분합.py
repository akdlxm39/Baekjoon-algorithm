import sys
input = sys.stdin.readline

def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = n+1
    tmp = nums[0]
    left = right = 0
    while True:
        if tmp < s:
            right += 1
            if right == n: break
            tmp += nums[right]
        else:
            tmp -= nums[left]
            ans = min(ans, right-left+1)
            left += 1
    print(ans if ans<=n else 0)

if __name__ == "__main__":
    main()