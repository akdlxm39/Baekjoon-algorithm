import sys
input = sys.stdin.readline

def all_kind_sum(sub):
    res = {0:1}
    for num in sub:
        for x, cnt in tuple(res.items()):
            res[x+num] = res.get(x+num, 0) + cnt
    return res

def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    left_sub, right_sub = nums[:n//2], nums[n//2:]
    left_sum = all_kind_sum(left_sub)
    right_sum = all_kind_sum(right_sub)
    ans = 0
    for left in left_sum:
        right = s - left
        if right in right_sum:
            ans += left_sum[left]*right_sum[right]
    print(ans if s!=0 else ans-1)

if __name__ == "__main__":
    main()