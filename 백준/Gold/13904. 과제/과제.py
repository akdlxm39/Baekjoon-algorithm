import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def main():
    n = int(input())
    subject = [tuple(map(int, input().split())) for _ in range(n)]
    sub = dict()
    for d, w in subject:
        if d in sub:
            sub[d].append(-w)
        else:
            sub[d] = [0, -w]
    answer = 0
    heap = []
    for d in range(max(sub.keys()), 0, -1):
        if d in sub:
            for x in sub[d]:
                heappush(heap, x)
        if heap:
            answer -= heappop(heap)
    print(answer)

if __name__ == "__main__":
    main()