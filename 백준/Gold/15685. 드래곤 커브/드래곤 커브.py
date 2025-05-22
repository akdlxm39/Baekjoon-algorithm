import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def dragon_curve(matrix, x, y, dirs, g):
    if g == 0:
        for d in dirs:
            nx, ny = x + dx[d], y + dy[d]
            matrix[nx][ny] = 1
            x, y = nx, ny
        return
    n_dirs = []
    for d in reversed(dirs):
        n_dirs.append((d+1)%4)
    dragon_curve(matrix, x, y, dirs+n_dirs, g-1)

def main():
    n =  int(input())
    matrix = [[0 for _ in range(101)] for _ in range(101)]
    for _ in range(n):
        x, y, d, g = map(int, input().split())
        matrix[x][y] = 1
        dragon_curve(matrix, x, y, [d], g)
    ans = 0
    for i in range(100):
        for j in range(100):
            if matrix[i][j] and matrix[i][j+1] and matrix[i+1][j] and matrix[i+1][j+1]:
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()