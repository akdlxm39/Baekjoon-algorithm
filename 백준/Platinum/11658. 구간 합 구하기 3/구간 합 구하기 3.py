import sys

input = sys.stdin.readline


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
    nums_2d = [[]]
    tree_2d = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        tmp = [0] + list(map(int, input().split()))
        for j in range(1, n + 1):
            update_2d(n, tree_2d, i, j, tmp[j])
        nums_2d.append(tmp)
    ans = []
    for _ in range(m):
        w, *command = map(int, input().split())
        if w == 0:
            a, b, c = command
            update_2d(n, tree_2d, a, b, c - nums_2d[a][b])
            nums_2d[a][b] = c
        else:
            x1, y1, x2, y2 = command
            ans.append(range_sum_2d(tree_2d, x1, y1, x2, y2))

    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    main()
