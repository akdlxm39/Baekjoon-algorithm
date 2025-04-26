import sys
input = sys.stdin.readline

def sum(tree, node, left, right, start, end):
    if end < left or start > right:
        return 0
    if start <= left and end >= right:
        return tree[node]
    mid = (left + right) // 2
    return (sum(tree, node*2, left, mid, start, end)
            + sum(tree, node*2 + 1, mid + 1, right, start, end))

def update(tree, node, left, right, idx):
    if left <= idx <= right:
        tree[node] += 1
        if left == right:
            return
        mid = (left + right) // 2
        update(tree, node*2, left, mid, idx)
        update(tree, node*2 + 1, mid + 1, right, idx)

def main():
    n = int(input())
    A = sorted(enumerate(map(int, input().split())), key=lambda x: x[1])
    seg_tree = [0]*(n*4)
    ans = 0
    for i, x in A:
        ans += sum(seg_tree, 1, 0, n-1, i+1, n-1)
        update(seg_tree, 1, 0, n-1, i)
    print(ans)



if __name__ == "__main__":
    main()