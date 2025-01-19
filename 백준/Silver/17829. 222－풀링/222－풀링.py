import sys
input = sys.stdin.readline

def solve(matrix, size, x, y):
    if size == 1:
        return matrix[x][y]
    l = []
    for i in range(x, x+size, size//2):
        for j in range(y, y+size, size//2):
            l.append(solve(matrix, size//2, i, j))
    return sorted(l)[2]

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(solve(matrix, n, 0, 0))

if __name__ == "__main__":
    main()