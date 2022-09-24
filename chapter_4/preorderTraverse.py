from node import *


def preorderTraverse(node):
    print(node, end=' ')
    if node.left is not None:
        preorderTraverse(node.left)
    if node.right is not None:
        preorderTraverse(node.right)
    

if __name__ == "__main__":
    A, B, C, D, E, F, G, H = tree1()
    preorderTraverse(A)
