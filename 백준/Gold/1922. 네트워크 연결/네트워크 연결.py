import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    costs = sorted((tuple(map(int, input().split())) for _ in range(m)), key = lambda x : x[2])
    root = [x for x in range(n+1)]
    link = dict([(x, {x}) for x in range(1, n+1)])
    ans = 0
    for a, b, cost in costs:
        if root[a] == root[b]:
            continue
        ans += cost
        link[root[a]] |= (link[root[b]])
        if len(link[root[a]]) == n:
            break
        for x in link[root[b]]:
            root[x] = root[a]
    print(ans)

if __name__ == "__main__":
    main()