import sys
input = sys.stdin.readline

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    size = 1
    while size < n:
        for x in range(0, n, size*2):
            for y in range(0, n, size*2):
                matrix[x][y] = sorted([matrix[x][y], matrix[x][y + size], matrix[x + size][y], matrix[x + size][y + size]])[2]
        size *= 2
    print(matrix[0][0])

if __name__ == "__main__":
    main()