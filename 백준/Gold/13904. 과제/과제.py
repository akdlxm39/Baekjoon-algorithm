import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def main():
    n = int(input())
    subject = sorted([tuple(map(int, input().split())) for _ in range(n)], reverse=True)
    answer = 0
    heap = []
    idx = 0
    for d in range(subject[0][0], 0, -1):
        while idx < n and subject[idx][0] == d:
            heappush(heap, -subject[idx][1])
            idx += 1
        if heap:
            answer -= heappop(heap)
    print(answer)

if __name__ == "__main__":
    main()