import sys
sys.setrecursionlimit(int(1e7))
input = sys.stdin.readline

def find(root, a):
    if a != root[a]:
        root[a] = find(root, root[a])
    return root[a]

def union(root, a, b):
    ar = find(root, a)
    br = find(root, b)
    if ar == br: return False
    root[br] = ar
    return True

def main():
    v, e = map(int, input().split())
    edges = []
    for _ in range(e):
        a, b, w = map(int, input().split())
        edges.append((w, a-1, b-1))
    edges.sort()
    root = list(range(v))
    total = 0
    need = v-1
    for w, a, b in edges:
        if union(root, a, b):
            total += w
            need -= 1
            if need == 0:
                break
    print(total)

if __name__ == "__main__":
    main()