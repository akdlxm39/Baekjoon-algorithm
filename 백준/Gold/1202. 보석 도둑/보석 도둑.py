import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    jewels = dict()
    for _ in range(n):
        m, v = map(int, input().split())
        if m in jewels:
            jewels[m].append(-v)
        else:
            jewels[m] = [-v]
    jewels_m = sorted(jewels.keys())
    bags = sorted(int(input()) for _ in range(k))
    can_put = []
    ans = index = 0
    for bag in bags:
        while index < len(jewels_m) and jewels_m[index] <= bag:
            for x in jewels[jewels_m[index]]:
                heappush(can_put, x)
            index += 1
        if can_put:
            ans -= heappop(can_put)
    print(ans)

if __name__ == "__main__":
    main()