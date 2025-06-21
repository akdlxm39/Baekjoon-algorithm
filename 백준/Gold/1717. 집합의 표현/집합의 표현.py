import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline

def find(root, a):
    if root[a] != a:
        root[a] = find(root, root[a])
    return root[a]

def union(root, a, b):
    ra = find(root, a)
    rb = find(root, b)
    root[ra] = rb

def main():
    n, m = map(int, input().split())
    root = list(range(n+1))
    for _ in range(m):
        c, a, b = map(int, input().split())
        if c == 0:
            union(root, a, b)
        elif c == 1:
            print('yes' if find(root, a) == find(root, b) else 'no')

if __name__ == "__main__":
    main()