import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
    ans = -1
    for i in range(n):
        for j in range(m):
            for di in range(-i, n-i):
                for dj in range(-j, m-j):
                    cur = 0
                    if di == 0 and dj == 0:
                        if arr[i][j] > ans and arr[i][j] in [0, 1, 4, 9]:
                            ans = arr[i][j]
                    else:
                        x, y = i, j
                        while 0<=x<n and 0<=y<m:
                            cur *= 10
                            cur += arr[x][y]
                            if cur > ans and int(cur ** 0.5) ** 2 == cur:
                                ans = cur
                            x += di
                            y += dj

    print(ans)
if __name__ == "__main__":
    main()