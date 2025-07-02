import sys
from heapq import heappushpop
input = sys.stdin.readline

def main():
    n = int(input())
    heap = list(map(int, input().split()))
    for _ in range(n-1):
        for num in sorted(map(int, input().split())):
            heappushpop(heap, num)
    print(heap[0])

if __name__ == "__main__":
    main()