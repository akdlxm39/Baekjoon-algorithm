import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

# 60 ~ 335
def main():
    n = int(input())
    month = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    flowers = []
    heap = []
    idx = 0
    for _ in range(n):
        m1, d1, m2, d2 = map(int, input().split())
        flowers.append((month[m1] + d1, month[m2] + d2))
        if flowers[-1][0] <= 60:
            heap.append(-flowers[-1][1])
            idx += 1
    flowers.sort()
    heapify(heap)

    cnt = 0
    while heap:
        cnt += 1
        cur = -heappop(heap)
        if cur >= 335:
            print(cnt)
            break
        while idx < n and flowers[idx][0] <= cur:
            heappush(heap, -flowers[idx][1])
            idx += 1
    else:
        print(0)
if __name__ == "__main__":
    main()