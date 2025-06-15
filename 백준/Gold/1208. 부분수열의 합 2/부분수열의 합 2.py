import sys
from collections import Counter
input = sys.stdin.readline

def all_kind_sum(sub):
    res = [0]
    for num in sub:
        tmp = [num+x for x in res]
        res += tmp
    return Counter(res[1:])

def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    left_sub, right_sub = nums[:n//2], nums[n//2:]
    left_sum = all_kind_sum(left_sub)
    right_sum = all_kind_sum(right_sub)
    ans = left_sum.get(s, 0) + right_sum.get(s, 0)
    for left in left_sum:
        right = s - left
        if right in right_sum:
            ans += left_sum[left]*right_sum[right]
    print(ans)

if __name__ == "__main__":
    main()