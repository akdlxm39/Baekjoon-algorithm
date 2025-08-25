import sys
from collections import deque

input = sys.stdin.readline
dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(n, m, cheese):
    queue = deque([(0, 0, 0)])
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 0
    ans_time = 0
    ans = 0
    while queue:
        time, cx, cy = queue.popleft()
        for dx, dy in dir:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] != -1:
                continue
            if cheese[nx][ny] == 1:
                visited[nx][ny] = time + 1
                queue.append((time + 1, nx, ny))
                if ans_time < time + 1:
                    ans_time = time + 1
                    ans = 1
                elif ans_time == time + 1:
                    ans += 1

            else:
                visited[nx][ny] = time
                queue.appendleft((time, nx, ny))
    return ans_time, ans


def main():
    n, m = map(int, input().split())
    cheese = [list(map(int, input().split())) for i in range(n)]
    print(*bfs(n, m, cheese), sep='\n')


if __name__ == "__main__":
    main()
