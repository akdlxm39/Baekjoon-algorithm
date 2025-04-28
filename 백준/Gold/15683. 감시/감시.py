import sys
input = sys.stdin.readline
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
cctv_dir_dict = {1: ((0,), (1,), (2,), (3,)),
                 2: ((0, 2),(1, 3)),
                 3: ((0, 1), (1, 2), (2, 3), (3, 0)),
                 4: ((0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)),
                 5: ((0, 1, 2, 3),)}

def watch_set(n, m, room, i, j, dir_idxes):
    res = set()
    for dir_idx in dir_idxes:
        dx, dy = directions[dir_idx]
        nx, ny = i + dx, j + dy
        while 0<=nx<n and 0<=ny<m and room[nx][ny] != 6:
            if room[nx][ny] == 0:
                res.add((nx, ny))
            nx += dx
            ny += dy
    return res

def bruteforce(n, m, room, cctv_sets, depth, seen_area, max_area):
    if depth == len(cctv_sets):
        max_area[0] = max(max_area[0], len(seen_area))
        return
    for cctv_set in cctv_sets[depth]:
        bruteforce(n, m, room, cctv_sets, depth + 1, seen_area | cctv_set, max_area)

def main():
    n, m = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(n)]
    cctv_sets = []
    blind = 0
    for i in range(n):
        for j in range(m):
            if room[i][j] == 0:
                blind += 1
            elif 1 <= room[i][j] <= 5:
                cctv_sets.append([watch_set(n, m, room, i, j, dir_idxes) for dir_idxes in cctv_dir_dict[room[i][j]]])
    max_area = [0]
    bruteforce(n, m, room, cctv_sets, 0, set(), max_area)
    print(blind-max_area[0])

if __name__ == "__main__":
    main()