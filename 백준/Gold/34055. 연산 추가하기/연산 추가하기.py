import sys
from bisect import bisect_left

input = sys.stdin.readline


def main():
    n, h = map(int, input().split())
    operations = sorted(tuple(map(int, input().split())) for _ in range(n))
    size_of_free_cycles = [0]
    cur = 0
    for s, e in operations:
        if cur < s - 1:
            size_of_free_cycles.append(s - 1 - cur)
        if cur < e:
            cur = e
    if cur < h:
        size_of_free_cycles.append(h - cur)
    num_of_free_cycles = len(size_of_free_cycles)
    size_of_free_cycles.sort()
    prefix_sum = [0]
    for i in range(1, num_of_free_cycles):
        prefix_sum.append(prefix_sum[-1] + size_of_free_cycles[i])
    q = int(input())
    ans = []
    for _ in range(q):
        t = int(input())
        if t > size_of_free_cycles[-1]:
            ans.append(0)
            continue
        idx = bisect_left(size_of_free_cycles, t)
        cnt = num_of_free_cycles - idx
        tmp = prefix_sum[-1] - (t - 1) * cnt
        if idx:
            tmp -= prefix_sum[idx - 1]
        ans.append(tmp)
    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    main()
