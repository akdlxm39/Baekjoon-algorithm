import sys
from collections import deque
input = sys.stdin.readline

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        parents = [0] * (n + 1)
        children = [[] for _ in range(n + 1)]
        depths = [-1] * (n + 1)
        for _ in range(n - 1):
            a, b = map(int, input().split())
            parents[b] = a
            children[a].append(b)
        root = min(range(1, n + 1), key=lambda x: parents[x])
        queue = deque([root])
        depths[root] = 0
        while queue:
            cur = queue.popleft()
            for nxt in children[cur]:
                depths[nxt] = depths[cur] + 1
                queue.append(nxt)
        x, y = map(int, input().split())
        while x != y:
            if depths[x] >= depths[y]:
                x = parents[x]
            else:
                y = parents[y]
        print(x)

if __name__ == "__main__":
    main()