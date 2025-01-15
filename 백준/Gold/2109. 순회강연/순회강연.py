import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def main():
    n = int(input())
    if n == 0:
        print(0)
        return
    lectures = [tuple(map(int, input().split())) for _ in range(n)]
    lectures.sort(key=lambda x: -x[1])
    heap = []
    idx = 0
    ans = 0
    for i in range(lectures[0][1], 0, -1):
        while idx < n and lectures[idx][1] == i:
            heappush(heap, -lectures[idx][0])
            idx += 1
        if heap:
            ans -= heappop(heap)
    print(ans)

if __name__ == "__main__":
    main()