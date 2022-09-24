from node import *


def inorderTraverse(node):
    if node.left is not None:
        inorderTraverse(node.left)
    print(node, end=' ')
    if node.right is not None:
        inorderTraverse(node.right)
    

if __name__ == "__main__":
    A, B, C, D, E, F, G, H = tree1()
    inorderTraverse(A)
