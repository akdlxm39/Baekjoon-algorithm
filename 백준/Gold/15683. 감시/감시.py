import sys
input = sys.stdin.readline
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cctv_dir_dict = {1: ((0,), (1,), (2,), (3,)),
                 2: ((0, 2),(1, 3)),
                 3: ((0, 1), (1, 2), (2, 3), (3, 0)),
                 4: ((0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)),
                 5: ((0, 1, 2, 3),)}

def cnt_blind_spot(n, m, room):
    cnt = 0
    for i in range(n):
        for j in range(m):
            cnt += room[i][j]==0
    return cnt

def watch(n, m, room, i, j, dir_idxes):
    new_room = [[room[x][y] for y in range(m)] for x in range(n)]
    for dir_idx in dir_idxes:
        dx, dy = directions[dir_idx]
        x, y = i + dx, j + dy
        while 0<=x<n and 0<=y<m and new_room[x][y] != 6:
            if new_room[x][y] == 0:
                new_room[x][y] = 7
            x += dx
            y += dy
    return new_room

def bruteforce(n, m, room, cctv, idx, ans):
    if idx == len(cctv):
        tmp = cnt_blind_spot(n, m, room)
        ans[0] = min(ans[0], tmp)
        return
    i, j, k = cctv[idx]
    for dir_idxes in cctv_dir_dict[k]:
        new_room = watch(n, m, room, i, j, dir_idxes)
        bruteforce(n, m, new_room, cctv, idx+1, ans)

def main():
    n, m = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    cctv = []
    for i in range(n):
        for j in range(m):
            if 1 <= room[i][j] <= 5:
                cctv.append((i, j, room[i][j]))
    ans = [n*m]
    bruteforce(n, m, room, cctv, 0, ans)
    print(ans[0])


if __name__ == "__main__":
    main()