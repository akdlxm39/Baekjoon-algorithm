import sys
input = sys.stdin.readline

def init(tree, node, left, right, sequence):
    if left == right:
        tree[node] = sequence[left-1]
        return
    mid = (left + right) // 2
    init(tree, node*2, left, mid, sequence)
    init(tree, node*2+1, mid+1, right, sequence)

def update(tree, node, left, right, start, end, delta):
    if right < start or end < left:
        return
    if start <= left and right <= end:
        tree[node] += delta
        return
    mid = (left + right) // 2
    update(tree, node*2, left, mid, start, end, delta)
    update(tree, node*2+1, mid+1, right, start, end, delta)

def get(tree, node, left, right, idx):
    if left == right:
        return tree[node]
    if tree[node]:
        tree[node*2] += tree[node]
        tree[node*2+1] += tree[node]
        tree[node] = 0
    mid = (left + right) // 2
    if left <= idx <= mid:
        return get(tree, node*2, left, mid, idx)
    else:
        return get(tree, node*2+1, mid+1, right, idx)

def main():
    n = int(input())
    sequence = list(map(int, input().split()))
    tree = [0]*(n*4)
    init(tree, 1, 1, n, sequence)
    m = int(input())
    answer = ''
    for _ in range(m):
        command = tuple(map(int, input().split()))
        if command[0] == 1:
            i, j, k = command[1:]
            update(tree, 1, 1, n, i, j, k)
        elif command[0] == 2:
            x = command[1]
            answer += str(get(tree, 1, 1, n, x)) + '\n'
    print(answer)

if __name__ == "__main__":
    main()