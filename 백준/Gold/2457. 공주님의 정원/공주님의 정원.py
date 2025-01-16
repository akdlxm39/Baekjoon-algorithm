import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline

# 60 ~ 335
def main():
    n = int(input())
    month = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    flowers = []
    new = 0
    idx = 0
    for _ in range(n):
        m1, d1, m2, d2 = map(int, input().split())
        if month[m1] + d1 <= 60:
            new = max(new, month[m2] + d2)
        else:
            flowers.append((month[m1] + d1, month[m2] + d2))
    flowers.sort()

    cnt = 0
    while True:
        cnt += 1
        cur = new
        if cur >= 335:
            print(cnt)
            break
        while idx < len(flowers) and flowers[idx][0] <= cur:
            new = max(new, flowers[idx][1])
            idx += 1
        if cur == new:
            print(0)
            break

if __name__ == "__main__":
    main()