import sys
from collections import deque

input = sys.stdin.readline


def bfs(n, conveni, visited, sx, sy, ex, ey):
    queue = deque([(sx, sy)])
    while queue:
        cx, cy = queue.popleft()
        if abs(cx - ex) + abs(cy - ey) <= 1000:
            return 'happy'
        for i, (nx, ny) in enumerate(conveni):
            if visited[i]: continue
            dist = abs(cx - nx) + abs(cy - ny)
            if dist > 1000: continue
            visited[i] = True
            queue.append((nx, ny))
    return 'sad'


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        sx, sy = map(int, input().split())
        conveni = [tuple(map(int, input().split())) for _ in range(n)]
        ex, ey = map(int, input().split())
        visited = [False] * n
        print(bfs(n, conveni, visited, sx, sy, ex, ey))


if __name__ == "__main__":
    main()
