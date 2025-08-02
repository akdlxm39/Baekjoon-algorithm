import sys

input = sys.stdin.readline


def show(tree):
    i = d = 1
    while len(tree) > i + d:
        print(tree[i:i + d])
        i += d
        d *= 2


def lazy_update(tree, lazy, node, length):
    if lazy[node]:
        tree[node] = length - tree[node]
        if length > 1:
            lazy[node * 2] = not lazy[node * 2]
            lazy[node * 2 + 1] = not lazy[node * 2 + 1]
        lazy[node] = False


def update(tree, lazy, node, left, right, start, end):
    length = right - left + 1
    lazy_update(tree, lazy, node, length)
    if right < start or end < left:
        return
    if start <= left and right <= end:
        tree[node] = length - tree[node]
        if left < right:
            lazy[node * 2] = not lazy[node * 2]
            lazy[node * 2 + 1] = not lazy[node * 2 + 1]
    else:
        mid = (left + right) // 2
        update(tree, lazy, node * 2, left, mid, start, end)
        update(tree, lazy, node * 2 + 1, mid + 1, right, start, end)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


def range_sum(tree, lazy, node, left, right, start, end):
    lazy_update(tree, lazy, node, right - left + 1)
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return (range_sum(tree, lazy, node * 2, left, mid, start, end) +
            range_sum(tree, lazy, node * 2 + 1, mid + 1, right, start, end))


def main():
    n, m = map(int, input().split())
    tree = [0] * (n * 4)
    lazy = [False] * (n * 4)
    ans = []
    for _ in range(m):
        o, s, t = map(int, input().split())
        if o == 0:
            update(tree, lazy, 1, 1, n, s, t)
        else:
            ans.append(range_sum(tree, lazy, 1, 1, n, s, t))
    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    main()
