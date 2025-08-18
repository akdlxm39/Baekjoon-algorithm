import sys
from collections import deque

input = sys.stdin.readline


def main():
    n, d = map(int, input().split())
    dp = list(map(int, input().split()))
    queue = deque()
    for i in range(n):
        dp[i] += dp[queue[0]] if queue and dp[queue[0]] > 0 else 0
        while queue and dp[queue[-1]] < dp[i]:
            queue.pop()
        queue.append(i)
        if queue[0] == i - d:
            queue.popleft()
    print(max(dp))


if __name__ == "__main__":
    main()
