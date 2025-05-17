import sys
input = sys.stdin.readline

def update(tree, node, left, right, idx):
    tree[node] += 1
    if left == right:
        return
    mid = (left + right) // 2
    if left <= idx <= mid:
        update(tree, node*2, left, mid, idx)
    else:
        update(tree, node*2+1, mid+1, right, idx)

def sum(tree, node, left, right, start, end):
    if end < left or right < start:
        return 0
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return (sum(tree, node*2, left, mid, start, end)
            + sum(tree, node*2+1, mid+1, right, start, end))

def main():
    n = int(input())
    ans = 0
    tree = [0] * (n * 4)
    mapping = {}
    for i, m in enumerate(map(int, input().split()), 1):
        mapping[m] = i
    list = []
    for i, m in enumerate(map(int, input().split()), 1):
        list.append((mapping[m], i))
    list.sort()
    for _, i in list:
        if i < n:
            ans += sum(tree, 1, 1, n, i+1, n)
        update(tree, 1, 1, n, i)
    print(ans)

if __name__ == "__main__":
    main()