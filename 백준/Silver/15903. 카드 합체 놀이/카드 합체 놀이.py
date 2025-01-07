import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    heapify(cards)
    for _ in range(m):
        x = heappop(cards) + heappop(cards)
        heappush(cards, x)
        heappush(cards, x)
    print(sum(cards))

if __name__ == "__main__":
    main()