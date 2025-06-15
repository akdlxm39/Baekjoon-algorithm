import sys
from collections import deque
input = sys.stdin.readline

def main():
    k = int(input())
    w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[-1]*w for _ in range(h)] # by_left_horse_move
    queue = deque([(0, 0, 0, k)]) # x, y, move_count, left_k
    visited[0][0] = 0
    while queue:
        cx, cy, cnt, left_k = queue.popleft()
        if cx == h - 1 and cy == w - 1:
            print(cnt)
            break
        cnt += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = dx + cx, dy + cy
            if not (0<=nx<h and 0<=ny<w): continue
            if visited[nx][ny] >= left_k or board[nx][ny] == 1: continue
            visited[nx][ny] = left_k
            queue.append((nx, ny, cnt, left_k))
        left_k -= 1
        for dx, dy in [(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2)]:
            nx, ny = dx + cx, dy + cy
            if not (0<=nx<h and 0<=ny<w): continue
            if visited[nx][ny] >= left_k or board[nx][ny] == 1: continue
            visited[nx][ny] = left_k
            queue.append((nx, ny, cnt, left_k))
    else:
        print(-1)


if __name__ == "__main__":
    main()