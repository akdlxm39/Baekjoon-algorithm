import sys
input = sys.stdin.readline
x, y = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(x)]
B = [list(map(int, input().split())) for _ in range(x)]
answer = [[A[i][j] + B[i][j] for j in range(y)] for i in range(x)]
for row in answer:
    print(*row)