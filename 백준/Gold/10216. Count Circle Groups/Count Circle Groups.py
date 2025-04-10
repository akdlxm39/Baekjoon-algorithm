import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def union(root, i, j):
    root[find(root, i)] = find(root, j)

def find(root, i):
    if root[i] != i:
        root[i] = find(root, root[i])
    return root[i]

def main():
    for _ in range(int(input())):
        n = int(input())
        x, y, r = [0]*n, [0]*n, [0]*n
        for i in range(n):
            x[i], y[i], r[i] = map(int, input().split())
        root = list(range(n))
        for i in range(1, n):
            for j in range(i):
                if (r[i] + r[j]) * (r[i] + r[j]) >= (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j]):
                    union(root, i, j)
        ans = 0
        for i in range(n):
            ans += i==root[i]
        print(ans)

if __name__ == "__main__":
    main()