from node import *


def preOrderFind8LetterNames(node):
    print(f"Visiting node {node}...")

    if len(str(node)) == 8:
        print(f'Found {node}')

    if node.left is not None:
        preOrderFind8LetterNames(node.left)
    if node.right is not None:
        preOrderFind8LetterNames(node.right)


def postOrderFind8LetterNames(node):

    if node.left is not None:
        postOrderFind8LetterNames(node.left)
    if node.right is not None:
        postOrderFind8LetterNames(node.right)

    print(f"Visiting node {node}...")
    if len(str(node)) == 8:
        print(f'Found {node}')


def inOrderFind8LetterNames(node):

    if node.left is not None:
        inOrderFind8LetterNames(node.left)

    print(f"Visiting node {node}...")
    if len(str(node)) == 8:
        print(f'Found {node}')

    if node.right is not None:
        inOrderFind8LetterNames(node.right)



if __name__ == "__main__":
    A, B, C, D, E, F, G, H = tree2()

    print("Pre-Order.")
    preOrderFind8LetterNames(A)

    print("Post-Order")
    postOrderFind8LetterNames(A)

    print("In-Order")
    inOrderFind8LetterNames(A)
    
    
