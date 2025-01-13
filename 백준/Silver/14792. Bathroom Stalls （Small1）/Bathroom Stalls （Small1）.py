import sys
from collections import deque
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def main():
    gap = lambda x: ((x - 1) // 2 + (x - 1) % 2, (x - 1) // 2)
    T = int(input())
    for i in range(1, T + 1):
        n, k = map(int, input().split())
        heap = [-n]
        max_gap = min_gap = 0
        for _ in range(k):
            cur = -heappop(heap)
            max_gap, min_gap = gap(cur)
            if max_gap != 0:
                heappush(heap, -max_gap)
                if min_gap != 0:
                    heappush(heap, -min_gap)
        print(f"Case #{i}:", max_gap, min_gap)

if __name__ == "__main__":
    main()