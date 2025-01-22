import sys
input = sys.stdin.readline

def postorder(preorder, inorder):
    if len(preorder) <= 1:
        return preorder
    idx = inorder.index(preorder[0])
    return (postorder(preorder[1:idx + 1], inorder[:idx]) +
            postorder(preorder[idx + 1:], inorder[idx + 1:]) +
            inorder[idx])

def main():
    while True:
        try:
            preorder, inorder = input().split()
        except:
            break
        postorder(preorder, inorder)
        print(postorder(preorder, inorder))

#preorder = cur, left, right
#inorder = left, cur, right
#postorder = left, right, cur

if __name__ == "__main__":
    main()