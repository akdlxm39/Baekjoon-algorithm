import sys
input = sys.stdin.readline

def union(root, i, j):
    root[find(root, i)] = find(root, j)

def find(root, i):
    if root[i] != i:
        root[i] = find(root, root[i])
    return root[i]

def main():
    for _ in range(int(input())):
        n = int(input())
        circles = [tuple(map(int, input().split())) for _ in range(n)]
        root = list(range(n))
        for i in range(1, n):
            x1, y1, r1 = circles[i]
            for j in range(i):
                if find(root, i) == find(root, j):
                    continue
                x2, y2, r2 = circles[j]
                if (r1 + r2) * (r1 + r2) >= (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1):
                    union(root, i, j)
        ans = 0
        for i in range(n):
            ans += i==root[i]
        print(ans)

if __name__ == "__main__":
    main()