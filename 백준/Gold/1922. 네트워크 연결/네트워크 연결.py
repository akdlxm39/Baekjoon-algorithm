import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, m = int(input()), int(input())
    costs = sorted((tuple(map(int, input().split())) for _ in range(m)), key = lambda x : x[2])
    link1 = [x for x in range(n+1)]
    link2 = dict([(x, [x]) for x in range(1, n+1)])
    ans = 0
    for a, b, cost in costs:
        if link1[a] == link1[b]:
            continue
        ans += cost
        for x in link2[link1[b]]:
            link2[link1[a]].append(x)
            link1[x] = link1[a]
    print(ans)

if __name__ == "__main__":
    main()