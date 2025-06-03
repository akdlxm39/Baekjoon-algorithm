import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def main():
    n = int(input())
    l = [int(input()) for _ in range(n)]
    ans = 0
    heapify(l)
    for _ in range(n-1):
        s = heappop(l) + heappop(l)
        ans += s
        heappush(l, s)
    print(ans)

if __name__ == "__main__":
    main()