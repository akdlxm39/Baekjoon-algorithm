import sys

input = sys.stdin.readline


def init(tree, node, left, right, nums):
    if left == right:
        tree[node] = nums[left]
    else:
        mid = (left + right) // 2
        tree[node] = (init(tree, node * 2, left, mid, nums)
                      ^ init(tree, node * 2 + 1, mid + 1, right, nums))
    return tree[node]


def lazy_update(tree, lazy, node, left, right):
    if lazy[node]:
        if (right - left + 1) % 2:
            tree[node] ^= lazy[node]
        if left != right:
            lazy[node * 2] ^= lazy[node]
            lazy[node * 2 + 1] ^= lazy[node]
        lazy[node] = 0


def update(tree, lazy, node, left, right, start, end, k):
    lazy_update(tree, lazy, node, left, right)
    if right < start or end < left:
        return
    if start <= left and right <= end:
        if (right - left + 1) % 2:
            tree[node] ^= k
        if left != right:
            lazy[node * 2] ^= k
            lazy[node * 2 + 1] ^= k
        return
    mid = (left + right) // 2
    update(tree, lazy, node * 2, left, mid, start, end, k)
    update(tree, lazy, node * 2 + 1, mid + 1, right, start, end, k)
    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]


def query(tree, lazy, node, left, right, start, end):
    lazy_update(tree, lazy, node, left, right)
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return (query(tree, lazy, node * 2, left, mid, start, end)
            ^ query(tree, lazy, node * 2 + 1, mid + 1, right, start, end))


def main():
    n = int(input())
    tree = [0] * (n * 4)
    lazy = [0] * (n * 4)
    nums = list(map(int, input().split()))
    init(tree, 1, 0, n - 1, nums)
    m = int(input())
    ans = []
    for _ in range(m):
        q, i, j, *k = tuple(map(int, input().split()))
        if q == 1:
            update(tree, lazy, 1, 0, n - 1, i, j, k[0])
        elif q == 2:
            ans.append(query(tree, lazy, 1, 0, n - 1, i, j))
    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    main()
