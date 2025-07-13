import sys
input = sys.stdin.readline

def dist(a, bx, by):
    return (a[0] - bx) ** 2 + (a[1] - by) ** 2

def find(root, a):
    if root[a] != a:
        root[a] = find(root, root[a])
    return root[a]

def union(root, a, b):
    ar = find(root, a)
    br = find(root, b)
    if ar != br:
        root[br] = ar
        return True
    return False

def main():
    n = int(input())
    stars = []
    lines = []
    for i in range(n):
        x, y = map(float, input().split())
        for j in range(i):
            lines.append((dist(stars[j], x, y), j, i))
        stars.append((x, y))
    ans = 0.0
    root = list(range(n))
    lines.sort()
    for d, a, b in lines:
        if union(root, a, b):
            ans += d ** 0.5
    print(ans)

if __name__ == "__main__":
    main()