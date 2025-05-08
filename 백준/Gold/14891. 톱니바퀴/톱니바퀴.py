import sys
input = sys.stdin.readline

def rotation(cogwheels, pivots, a, d, infer):
    if infer <= 0 and 0 < a and cogwheels[a][pivots[a][1]] != cogwheels[a-1][pivots[a-1][2]]:
        rotation(cogwheels, pivots, a-1, -d, -1)
    if infer >= 0 and a < 3 and cogwheels[a][pivots[a][2]] != cogwheels[a+1][pivots[a+1][1]]:
        rotation(cogwheels, pivots, a+1, -d, 1)
    for i in range(3):
        pivots[a][i] = (pivots[a][i] - d) % 8

def main():
    cogwheels = [input().rstrip() for _ in range(4)]
    pivots = [[0, 6, 2] for _ in range(4)]
    n = int(input())
    for _ in range(n):
        a, d = map(int, input().split())
        rotation(cogwheels, pivots, a-1, d, 0)
    ans = 0
    for i in range(4):
        if cogwheels[i][pivots[i][0]] == '1':
            ans += 2**i
    print(ans)

if __name__ == "__main__":
    main()