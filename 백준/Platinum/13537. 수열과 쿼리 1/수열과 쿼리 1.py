import sys
from bisect import bisect_right

input = sys.stdin.readline


def merge_sort(sort_tree, node, left_node, right_node):
    left_size = len(sort_tree[left_node])
    right_size = len(sort_tree[right_node])
    i, j = 0, 0
    while i < left_size and j < right_size:
        if sort_tree[left_node][i] < sort_tree[right_node][j]:
            sort_tree[node].append(sort_tree[left_node][i])
            i += 1
        else:
            sort_tree[node].append(sort_tree[right_node][j])
            j += 1
    while i < left_size:
        sort_tree[node].append(sort_tree[left_node][i])
        i += 1
    while j < right_size:
        sort_tree[node].append(sort_tree[right_node][j])
        j += 1


def init(sort_tree, node, left, right, nums):
    if left == right:
        sort_tree[node].append(nums[left - 1])
    else:
        mid = (left + right) // 2
        init(sort_tree, node * 2, left, mid, nums)
        init(sort_tree, node * 2 + 1, mid + 1, right, nums)
        merge_sort(sort_tree, node, node * 2, node * 2 + 1)


def query(sort_tree, node, left, right, start, end, num):
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return right - left + 1 - bisect_right(sort_tree[node], num)
    mid = (left + right) // 2
    return (query(sort_tree, node * 2, left, mid, start, end, num) +
            (query(sort_tree, node * 2 + 1, mid + 1, right, start, end, num)))


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    size = 2 ** ((n - 1).bit_length() + 2)
    sort_tree = [[] for _ in range(size)]
    init(sort_tree, 1, 1, n, nums)
    m = int(input())
    ans = []
    for _ in range(m):
        i, j, k = map(int, input().split())
        ans.append(query(sort_tree, 1, 1, n, i, j, k))
    print('\n'.join(map(str, ans)))


if __name__ == "__main__":
    main()
