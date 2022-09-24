from tree import Tree

if __name__ == "__main__":
    A = Tree()
    B = Tree()
    C = Tree("C")
    print(A, B, C, Tree._id)
    del C
    print(A, B, Tree._id)
