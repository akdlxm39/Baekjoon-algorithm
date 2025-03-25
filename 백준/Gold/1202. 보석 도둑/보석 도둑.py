import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def lower_bound(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if x >= arr[mid][0]:
            l = mid+1
        else:
            r = mid-1
    return l

def main():
    n, k = map(int, input().split())
    jewels = sorted(tuple(map(int, input().split())) for _ in range(n))
    bags = sorted(int(input()) for _ in range(k))
    can_put = []
    ans = l = 0
    for bag in bags:
        r = lower_bound(jewels, bag)
        for _, v in jewels[l:r]:
            heappush(can_put, -v)
        l = r
        if can_put:
            ans -= heappop(can_put)
    print(ans)

if __name__ == "__main__":
    main()