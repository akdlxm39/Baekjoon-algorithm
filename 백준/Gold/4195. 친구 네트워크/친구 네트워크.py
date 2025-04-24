import sys
input = sys.stdin.readline

def union(parent, a, b):
    root_a, root_b = find(parent, a), find(parent, b)
    if root_a != root_b:
        parent[root_a] += parent[root_b]
        parent[root_b] = root_a
    return parent[root_a]


def find(parent, x):
    if isinstance(parent[x], str):
        parent[x] = find(parent, parent[x])
        return parent[x]
    else:
        return x

def main():
    t = int(input())
    for _ in range(t):
        f = int(input())
        parent = dict()
        for _ in range(f):
            a, b = input().split()
            parent.setdefault(a, 1)
            parent.setdefault(b, 1)
            print(union(parent, a, b))

if __name__ == "__main__":
    main()