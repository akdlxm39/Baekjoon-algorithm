import sys
input = sys.stdin.readline
dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]

def main():
    n, m, k = map(int, input().split())
    map_ = [list(map(int, input().split())) for _ in range(n)]
    sharks_location = [(0,0)]*(m+1)
    for i in range(n):
        for j in range(n):
            if map_[i][j]:
                sharks_location[map_[i][j]] = (i, j)
                map_[i][j] = (map_[i][j], k)
            else:
                map_[i][j] = (0, 0)
    sharks_dir = [0] + list(map(int, input().split()))
    sharks_moves = [[[]]] + [[[]]+[list(map(int, input().split())) for _ in range(4)] for _ in range(m)]
    time = 0
    sharks_count = m-1
    while sharks_count > 0 and time <= 1000:
        next_moves = [(-1, -1)]*(m+1)
        for shark_idx in range(1, m + 1):
            x, y = sharks_location[shark_idx]
            if x == -1 and y == -1: continue
            for dir in sharks_moves[shark_idx][sharks_dir[shark_idx]]:
                nx, ny = x+dx[dir], y+dy[dir]
                if not (0<=nx<n and 0<=ny<n): continue
                if map_[nx][ny][0]: continue
                next_moves[shark_idx] = (nx, ny)
                sharks_dir[shark_idx] = dir
                break
            else:
                for dir in sharks_moves[shark_idx][sharks_dir[shark_idx]]:
                    nx, ny = x + dx[dir], y + dy[dir]
                    if not (0 <= nx < n and 0 <= ny < n): continue
                    if map_[nx][ny][0] != shark_idx: continue
                    next_moves[shark_idx] = (nx, ny)
                    sharks_dir[shark_idx] = dir
                    break
        for i in range(n):
            for j in range(n):
                shark_idx, smell = map_[i][j]
                if smell == 0: continue
                smell -= 1
                if smell:
                    map_[i][j] = (shark_idx, smell)
                else:
                    map_[i][j] = (0, 0)
        for shark_idx in range(1, m + 1):
            x, y = next_moves[shark_idx]
            if x == -1 and y == -1: continue
            if map_[x][y][0] == 0 or map_[x][y][0] == shark_idx:
                sharks_location[shark_idx] = (x, y)
                map_[x][y] = (shark_idx, k)
            else:
                sharks_count -= 1
                sharks_location[shark_idx] = (-1, -1)
        time += 1
    print(time if time < 1001 else -1)

if __name__ == "__main__":
    main()