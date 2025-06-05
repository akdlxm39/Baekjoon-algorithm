import sys
input = sys.stdin.readline
dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def shark_move(map_, fishes, x, y, cnt):
    new_map_ = [[fish for fish in line] for line in map_]
    new_fishes = [fish for fish in fishes]

    d, n = shark_eat(new_map_, new_fishes, x, y)
    dx, dy = dirs[d]
    cnt += n
    fish_move(new_map_, new_fishes, x, y)

    res = []
    nx, ny = x + dx, y + dy
    while 0<=nx<4 and 0<=ny<4:
        if new_map_[nx][ny] != 0:
            res.append(shark_move(new_map_, new_fishes, nx, ny, cnt))
        nx, ny = nx + dx, ny + dy
    if res:
        return max(res)
    else:
        return cnt

def shark_eat(map_, fishes, x, y):
    fish_ate = map_[x][y]
    map_[x][y] = 0
    d = fishes[fish_ate][2]
    fishes[fish_ate] = None
    return d, fish_ate

def fish_move(map_, fishes, x, y):
    for a in range(1, 17):
        if not fishes[a]: continue
        cx, cy, cd = fishes[a]
        for dd in range(8):
            nd = (cd + dd) % 8
            nx, ny = cx + dirs[nd][0], cy + dirs[nd][1]
            if not (0<=nx<4 and 0<=ny<4) or (nx==x and ny==y): continue
            if map_[nx][ny]==0:
                fishes[a] = (nx, ny, nd)
                map_[cx][cy], map_[nx][ny] = 0, a
            else:
                b = map_[nx][ny]
                fishes[a], fishes[b] = (nx, ny, nd), (cx, cy, fishes[b][2])
                map_[cx][cy], map_[nx][ny] = b, a
            break

def main():
    fishes = [(0, 0, 0)]*18
    map_ = [[0]*4 for _ in range(4)]
    for i in range(4):
        line = list(map(int, input().split()))
        for j in range(4):
            map_[i][j] = line[2*j]
            fishes[line[2*j]] = (i, j, line[2*j+1]-1)
    ans = shark_move(map_, fishes, 0, 0, 0)
    print(ans)

if __name__ == "__main__":
    main()