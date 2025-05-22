import sys
input = sys.stdin.readline
INF = int(1e10)

def init(tree, node, left, right):
    if left == right:
        tree[node] = int(input())
        return tree[node]
    mid = (left+right)//2
    tree[node] = min(init(tree, node*2, left, mid),
                     init(tree, node*2+1, mid+1, right))
    return tree[node]

def get(tree, node, left, right, start, end):
    if end < left or right < start:
        return INF
    if start <= left and right <= end:
        return tree[node]
    mid = (left+right)//2
    return min(get(tree, node*2, left, mid, start, end),
               get(tree, node*2+1, mid+1, right, start, end))

def main():
    n, m = map(int, input().split())
    tree = [INF]*(n*4)
    init(tree, 1, 1, n)
    answers = []
    for _ in range(m):
        a, b = map(int, input().split())
        answers.append(get(tree, 1, 1, n, a, b))
    print('\n'.join(map(str, answers)))

if __name__ == "__main__":
    main()