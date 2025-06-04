import sys
input = sys.stdin.readline
dxdy = [(0,1), (0,-1), (1,0), (-1,0)]

def rotate(n, disks, x, d, k):
    if d==0:
        k = -k
    for xi in range(x-1, n, x):
        disks[xi] = disks[xi][k:] + disks[xi][:k]

def erase(n, m, disks, info):
    visited = [[False] * m for _ in range(n)]
    does_erase = False
    for i in range(n):
        for j in range(m):
            if visited[i][j]: continue
            visited[i][j] = True
            num = disks[i][j]
            if num == 0: continue
            queue = [(i, j)]
            size = 1
            pivot = 0
            while pivot < size:
                x, y = queue[pivot]
                for dx, dy in dxdy:
                    nx, ny = x + dx, (y + dy) % m
                    if not(0<=nx<n) or visited[nx][ny] or disks[nx][ny] != num: continue
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    size += 1
                pivot += 1
            if size > 1:
                does_erase = True
                info[0] -= size
                info[1] -= size*num
                for x, y in queue:
                    disks[x][y] = 0
    return does_erase

def convert(n, m, disks, info):
    if erase(n, m, disks, info):
        return
    if info[0] == 0:
        return
    mean = info[1]/info[0]
    for i in range(n):
        for j in range(m):
            if 0<disks[i][j]<mean:
                disks[i][j] += 1
                info[1] += 1
            elif disks[i][j]>mean:
                disks[i][j] -= 1
                info[1] -= 1

def main():
    n, m, t = map(int, input().split())
    disks = []
    info = [n*m, 0]
    for _ in range(n):
        disk = list(map(int, input().split()))
        info[1] += sum(disk)
        disks.append(disk)
    for _ in range(t):
        x, d, k = map(int, input().split())
        rotate(n, disks, x, d, k)
        convert(n, m, disks, info)

    print(info[1])

if __name__ == "__main__":
    main()