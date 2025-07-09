import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def main():
    n = int(input())
    problems = sorted((tuple(map(int, input().split())) for _ in range(n)), reverse=True)
    heap = []
    ans = idx = 0
    for i in range(n, 0, -1):
        while idx < n and problems[idx][0] >= i:
            heappush(heap, -problems[idx][1])
            idx += 1
        if heap:
            ans -= heappop(heap)
    print(ans)

if __name__ == "__main__":
    main()