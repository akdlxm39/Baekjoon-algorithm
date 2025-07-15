import sys
from collections import deque
input = sys.stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(n, arr, snum, enum):
    queue = deque([(0, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny]: continue
            visited[nx][ny] = True
            if snum <= arr[nx][ny] <= enum:
                if nx == n - 1 and ny == n - 1: return True
                queue.append((nx, ny))
    return False

def main():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    start_num, end_num = min(arr[0][0], arr[-1][-1]), max(arr[0][0], arr[-1][-1])
    left, right = 0, 200
    while left < right:
        mid = (left + right) // 2
        for snum in range(max(end_num - mid, 0), start_num + 1):
            if bfs(n, arr, snum, snum + mid):
                right = mid
                break
        else:
            left = mid + 1
    print(left)

if __name__ == "__main__":
    main()