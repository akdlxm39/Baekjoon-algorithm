import sys

input = sys.stdin.readline


def main():
    n = int(input())
    nums = sorted(map(int, input().split()))
    count = {}
    zero = 0
    for num in nums:
        if num == 0:
            zero += 1
            continue
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    ans = 0
    make_zero = False
    for i in range(n - 1):
        if nums[i] == 0: continue
        for j in range(i + 1, n):
            if nums[j] == 0: continue
            x = nums[i] + nums[j]
            if x == 0:
                make_zero = True
            if x in count:
                ans += count[x]
                del count[x]
    if make_zero or zero >= 3:
        ans += zero
    if zero:
        for n, cnt in count.items():
            if cnt >= 2:
                ans += cnt
    print(ans)


if __name__ == "__main__":
    main()
