import sys
input = sys.stdin.readline

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    ans = 0
    for x in range(n):
        if ans < 4 and matrix[x][x] != 0:
            ans = 4
        for y in range(n):
            if ans < 3 and x != y and matrix[x][y] <= 0:
                ans = 3
            if ans < 2 and matrix[x][y] != matrix[y][x]:
                ans = 2
            for z in range(n):
                if ans < 1 and matrix[x][y] + matrix[y][z] < matrix[x][z]:
                    ans = 1
    print(5 - ans if ans else 0)

if __name__ == "__main__":
    main()