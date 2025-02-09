import sys
from heapq import heapify, heappush, heappop
input = sys.stdin.readline
INF = 987654321

def main():
    idx = 1
    while n := int(input()):
        maps = [list(map(int, input().split())) for _ in range(n)]
        dp = [[INF] * n for _ in range(n)]
        dp[0][0] = maps[0][0]
        heap = [(dp[0][0], 0, 0)]
        while heap:
            dist, cx, cy = heappop(heap)
            if -cx == n-1 and -cy == n-1:
                print(f"Problem {idx}: {dp[-1][-1]}")
                break
            delta = [(0,-1), (0, 1), (-1, 0), (1, 0)]
            for dx, dy in delta:
                nx, ny = -cx + dx, -cy + dy
                if not (0 <= nx < n and 0 <= ny < n) or dp[nx][ny] <= dist + maps[nx][ny]:
                    continue
                dp[nx][ny] = dist + maps[nx][ny]
                heappush(heap, (dp[nx][ny], -nx, -ny))
        idx += 1

if __name__ == "__main__":
    main()