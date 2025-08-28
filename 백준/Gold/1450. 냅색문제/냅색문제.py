import sys
from bisect import bisect_right
from itertools import combinations

input = sys.stdin.readline


def all_kind_sum(sub):
    res = []
    for i in range(len(sub) + 1):
        for x in combinations(sub, i):
            res.append(sum(x))
    return res


def main():
    n, c = map(int, input().split())
    weights = [x for x in map(int, input().split()) if x <= c]
    cnt = len(weights)
    left_sub, right_sub = weights[:cnt // 2], weights[cnt // 2:]
    left_sum, right_sum = all_kind_sum(left_sub), all_kind_sum(right_sub)
    right_sum.sort()
    ans = 0
    for l in left_sum:
        max_r = c - l
        ans += bisect_right(right_sum, max_r)
    print(ans)


if __name__ == "__main__":
    main()
