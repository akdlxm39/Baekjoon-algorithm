import sys

sys.setrecursionlimit(100007)
input = sys.stdin.readline


def find(root, x):
    if root[x][0] != x:
        rx, tmp = find(root, root[x][0])
        root[x] = (rx, root[x][1] + tmp)
    return root[x]


def union(root, a, b, gap):
    ra, agap = find(root, a)
    rb, bgap = find(root, b)
    if ra > rb:
        root[ra] = (rb, bgap - agap + gap)
    else:
        root[rb] = (ra, agap - bgap - gap)


def get(root, a, b):
    ra, agap = find(root, a)
    rb, bgap = find(root, b)
    if ra != rb:
        return 'UNKNOWN'
    return str(agap - bgap)


def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        root = [(i, 0) for i in range(n + 1)]
        ans = []
        for _ in range(m):
            command = input().split()
            if command[0] == '!':
                a, b, w = map(int, command[1:])
                union(root, a, b, w)
            elif command[0] == '?':
                a, b = map(int, command[1:])
                ans.append(get(root, a, b))
        print('\n'.join(ans))


if __name__ == "__main__":
    main()
