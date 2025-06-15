import sys
input = sys.stdin.readline

def all_kind_sum(size, sub, sum_sub, cur, idx):
    if idx == size:
        sum_sub[cur] = sum_sub.get(cur, 0) + 1
        return
    all_kind_sum(size, sub, sum_sub, cur, idx+1)
    all_kind_sum(size, sub, sum_sub, cur+sub[idx], idx+1)

def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))
    left_sub, right_sub = nums[:n//2], nums[n//2:]
    left_sum, right_sum = {}, {}
    all_kind_sum(len(left_sub), left_sub, left_sum, 0, 0)
    all_kind_sum(len(right_sub), right_sub, right_sum, 0, 0)
    left_sum[0] -= 1
    right_sum[0] -= 1
    ans = left_sum.get(s, 0) + right_sum.get(s, 0)
    for left in left_sum:
        right = s - left
        if right in right_sum:
            ans += left_sum[left]*right_sum[right]
    print(ans)

if __name__ == "__main__":
    main()