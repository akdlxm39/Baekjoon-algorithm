import sys
input = sys.stdin.readline
INF = int(1e9)
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def get_snail(n):
    w = h = 1
    idx = 1
    while idx + h <= n:
        idx += h
        if w == h: h += 1
        else: w += 1
    snail = [[-1] * (w + n - idx) for _ in range(h)]
    snail[-1] = list(range(idx - w, n))
    x, y = h - 1, 0

    di = 0
    num = idx - w - 1
    while num >= 0:
        h -= 1
        for _ in range(h):
            x, y = x + dx[di], y + dy[di]
            snail[x][y] = num
            num -= 1
        di = (di + 1) % 4
        w -= 1
        for _ in range(w):
            x, y = x + dx[di], y + dy[di]
            snail[x][y] = num
            num -= 1
        di = (di + 1) % 4
    return snail

def get_building(n):
    f = n // 4
    building = [
        list(range(f*3-1, f*2-1, -1)),
        list(range(f, f*2)),
        list(range(f-1, -1, -1)),
        list(range(f*3, f*4))
    ]
    return building

def step_1(nums, k):
    min_n = min(nums)
    max_n = max(nums)
    if abs(max_n - min_n) <= k:
        return False
    for i in range(len(nums)):
        if nums[i] == min_n:
            nums[i] += 1
    return True

def step_2_3(nums, container):
    w, h = len(container[0]), len(container)
    tmp = []
    for i in range(h):
        for j in range(w):
            if container[i][j] == -1: break
            cur = container[i][j]
            for di, dj in [[0, 1], [1, 0]]:
                ni, nj = i + di, j + dj
                if nj == w or ni == h or container[ni][nj] == -1: continue
                nxt = container[ni][nj]
                d = abs(nums[nxt] - nums[cur]) // 5
                if d:
                    if nums[nxt] > nums[cur]:
                        tmp.append((nxt, cur, d))
                    else:
                        tmp.append((cur, nxt, d))
    for a, b, d in tmp:
        nums[a] -= d
        nums[b] += d
    new_nums = []
    for j in range(w):
        for i in range(h-1, -1, -1):
            if container[i][j] == -1: break
            new_nums.append(nums[container[i][j]])
    return new_nums

def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    snail = get_snail(n)
    building = get_building(n)
    ans = 0
    while step_1(nums, k):
        nums = step_2_3(nums, snail)
        nums = step_2_3(nums, building)
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()