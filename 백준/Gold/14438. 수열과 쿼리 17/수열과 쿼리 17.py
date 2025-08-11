import sys

input = sys.stdin.readline
INF = int(1e9)


def show(tree):
    i = 1
    k = 1
    while i + k < len(tree):
        print(tree[i:i + k])
        i += k
        k *= 2


def init(tree, node, left, right, nums):
    if left == right:
        tree[node] = nums[left - 1]
    else:
        mid = (left + right) // 2
        tree[node] = min(init(tree, node * 2, left, mid, nums),
                         init(tree, node * 2 + 1, mid + 1, right, nums))
    return tree[node]


def update(tree, node, left, right, idx, num):
    if left == right:
        tree[node] = num
        return
    mid = (left + right) // 2
    if left <= idx <= mid:
        update(tree, node * 2, left, mid, idx, num)
    else:
        update(tree, node * 2 + 1, mid + 1, right, idx, num)
    tree[node] = min(tree[node * 2], tree[node * 2 + 1])


def range_min(tree, node, left, right, start, end):
    if right < start or end < left:
        return INF
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return min(range_min(tree, node * 2, left, mid, start, end),
               range_min(tree, node * 2 + 1, mid + 1, right, start, end))


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    tree = [INF] * (n * 4)
    init(tree, 1, 1, n, nums)
    m = int(input())
    answers = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        if a == 1:
            update(tree, 1, 1, n, b, c)
        elif a == 2:
            answers.append(range_min(tree, 1, 1, n, b, c))
    print('\n'.join(map(str, answers)))


if __name__ == "__main__":
    main()
