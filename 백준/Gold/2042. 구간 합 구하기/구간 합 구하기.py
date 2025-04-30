import sys
input = sys.stdin.readline

def init(seg_tree, node, left, right):
    if left == right:
        seg_tree[node] = int(input())
    else:
        mid = (left + right) // 2
        seg_tree[node] = (init(seg_tree, node*2, left, mid) +
                          init(seg_tree, node*2+1, mid+1, right))
    return seg_tree[node]

def update(seg_tree, node, left, right, idx, num):
    if left == right:
        gap = num - seg_tree[node]
    else:
        mid = (left + right) // 2
        if idx <= mid:
            gap = update(seg_tree, node * 2, left, mid, idx, num)
        else:
            gap = update(seg_tree, node * 2 + 1, mid + 1, right, idx, num)
    seg_tree[node] += gap
    return gap

def range_sum(seg_tree, node, left, right, start, end):
    if right < start or end < left:
        return 0
    if start <= left and right <= end:
        return seg_tree[node]
    mid = (left + right) // 2
    return (range_sum(seg_tree, node*2, left, mid, start, end) +
            range_sum(seg_tree, node*2+1, mid+1, right, start, end))

def main():
    n, m, k = map(int, input().split())
    seg_tree = [0] * (n*4)
    init(seg_tree, 1,1, n)
    ans = []
    for _ in range(m+k):
        a, b, c = map(int, input().split())
        if a == 1:
            update(seg_tree, 1, 1, n, b, c)
        elif a == 2:
            ans.append(range_sum(seg_tree, 1, 1, n, b, c))
    print('\n'.join(map(str, ans)))

if __name__ == "__main__":
    main()