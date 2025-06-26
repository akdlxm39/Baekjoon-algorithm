import sys
from heapq import heapify, heappop
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
    heap = []
    for _ in range(e):
        a, b, w = map(int, input().split())
        heap.append((w, a-1, b-1))
    heapify(heap)
    root = list(range(v))
    total = 0
    need = v-1
    while heap and need:
        w, a, b = heappop(heap)
        if union(root, a, b):
            total += w
            need -= 1
    print(total)

if __name__ == "__main__":
    main()