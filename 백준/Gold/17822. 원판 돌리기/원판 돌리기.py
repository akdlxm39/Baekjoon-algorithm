import sys
input = sys.stdin.readline
dxdy = [(0,1), (0,-1), (1,0), (-1,0)]

def rotate(n, disks, x, d, k):
    if d==0:
        k = -k
    for xi in range(x-1, n, x):
        disks[xi] = disks[xi][k:] + disks[xi][:k]

def erase(n, m, disks, info):
    queue = set()
    for i in range(n):
        for j in range(m):
            nj = (j + 1) % m
            if disks[i][j] != 0 and disks[i][j] == disks[i][nj]:
                queue.add((i, j))
                queue.add((i, nj))
    for i in range(n-1):
        for j in range(m):
            ni = i + 1
            if disks[i][j] != 0 and disks[i][j] == disks[ni][j]:
                queue.add((i, j))
                queue.add((ni, j))
    if queue:
        for x, y in queue:
            info[1] -= disks[x][y]
            disks[x][y] = 0
        info[0] -= len(queue)
        return True
    return False

def convert(n, m, disks, info):
    if info[0] == 0:
        return
    if erase(n, m, disks, info):
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