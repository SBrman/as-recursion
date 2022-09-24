from node import *


def getDepth(node):
    if node is None or (node.left is None and node.right is None):
        return 0
    else:
        return max(getDepth(node.left), getDepth(node.right)) + 1



if __name__ == "__main__":
    A, B, C, D, E, F, G, H = tree1()
    print(getDepth(A))
    print(getDepth(B))
    
    
