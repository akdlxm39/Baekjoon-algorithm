import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6+5)

def preorder(inorder, postorder, size, ini, posti):
    # print(inorder, postorder)
    # print(size, ini, posti)
    # print(inorder[ini:ini+size], postorder[posti:posti+size])
    idx = postorder[posti+size-1] - ini
    print(inorder[ini+idx], end=' ')
    if idx != 0:
        preorder(inorder, postorder, idx, ini, posti)
    if size-idx-1 != 0:
        preorder(inorder, postorder, size-idx-1, ini+idx+1, posti+idx)

def main():
    n = int(input())
    inorder = list(map(int, input().split()))
    inorder_dict = dict((x, i) for i, x in enumerate(inorder))
    postorder = list(map(int, input().split()))
    postorder = [inorder_dict[x] for x in postorder]
    preorder(inorder, postorder, n, 0, 0)

if __name__ == "__main__":
    main()