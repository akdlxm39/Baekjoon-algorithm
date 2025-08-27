import sys

input = sys.stdin.readline


def init_2d(n, tree_2d):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            j2 = j + (j & -j)
            if j2 <= n:
                tree_2d[i][j2] += tree_2d[i][j]
    for j in range(1, n + 1):
        for i in range(1, n + 1):
            i2 = i + (i & -i)
            if i2 <= n:
                tree_2d[i2][j] += tree_2d[i][j]


def update_2d(n, tree_2d, x, y, delta):
    while x <= n:
        cy = y
        while cy <= n:
            tree_2d[x][cy] += delta
            cy += cy & -cy
        x += x & -x


def sum_2d(tree_2d, x, y):
    res = 0
    while x > 0:
        cy = y
        while cy > 0:
            res += tree_2d[x][cy]
            cy -= cy & -cy
        x -= x & -x
    return res


def range_sum_2d(tree_2d, x1, y1, x2, y2):
    res = sum_2d(tree_2d, x2, y2)
    res -= sum_2d(tree_2d, x2, y1 - 1)
    res -= sum_2d(tree_2d, x1 - 1, y2)
    res += sum_2d(tree_2d, x1 - 1, y1 - 1)
    return res


def main():
    n, m = map(int, input().split())
    nums_2d = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
    tree_2d = [nums_2d[i][:] for i in range(n + 1)]
    init_2d(n, tree_2d)
    ans = []
    for _ in range(m):
        w, a, b, c, *d = map(int, input().split())
        if w == 0:
            update_2d(n, tree_2d, a, b, c - nums_2d[a][b])
            nums_2d[a][b] = c
        else:
            ans.append(range_sum_2d(tree_2d, a, b, c, d[0]))

    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    main()
