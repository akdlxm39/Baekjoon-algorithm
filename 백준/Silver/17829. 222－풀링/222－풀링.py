import sys
input = sys.stdin.readline

def solve(matrix, size, x, y):
    if size == 1:
        return matrix[x][y]
    new_size = size//2
    l = [solve(matrix, new_size, x, y), solve(matrix, new_size, x, y+new_size), solve(matrix, new_size, x+new_size, y), solve(matrix, new_size, x+new_size, y+new_size)]
    return sorted(l)[2]

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print(solve(matrix, n, 0, 0))

if __name__ == "__main__":
    main()