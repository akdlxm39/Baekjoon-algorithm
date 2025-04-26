import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, l = map(int, input().split())
    nums = list(map(int, input().split()))
    dq = deque()
    for i, num in enumerate(nums):
        while dq and num <= dq[-1][0]:
            dq.pop()
        dq.append((num, i+l-1))
        print(dq[0][0])
        if dq[0][1] == i:
            dq.popleft()

if __name__ == "__main__":
    main()