import sys
input = sys.stdin.readline

class Node():
    def __init__(self, value):
        self.value : int = value
        self.left : Node = None
        self.right : Node = None

def tree_recovery(preorder, inorder):
    if not preorder:
        return None
    node = Node(preorder[0])
    idx = inorder.index(preorder[0])
    node.left = tree_recovery(preorder[1:idx+1], inorder[:idx])
    node.right = tree_recovery(preorder[idx+1:], inorder[idx+1:])
    return node

def postordering(node, postorder):
    if not node:
        return
    postordering(node.left, postorder)
    postordering(node.right, postorder)
    postorder.append(node.value)

def main():
    while True:
        try:
            preorder, inorder = input().split()
        except:
            break
        tree = tree_recovery(preorder, inorder)
        ans = []
        postordering(tree, ans)
        print(''.join(ans))

#preorder = cur, left, right
#inorder = left, cur, right
#postorder = left, right, cur

if __name__ == "__main__":
    main()