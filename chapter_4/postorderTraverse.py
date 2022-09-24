from node import *


def postorderTraverse(node):
    if node.left is not None:
        postorderTraverse(node.left)
    if node.right is not None:
        postorderTraverse(node.right)
    print(node, end=' ')
    

if __name__ == "__main__":
    A, B, C, D, E, F, G, H = tree1()
    postorderTraverse(A)
