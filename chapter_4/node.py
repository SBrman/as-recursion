class Node:
    _id = 0

    def __init__(self, value=None):
        Node._id += 1
        self._id = Node._id

        self.value = value if value is not None else self._id
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node id={self.value}>"
    
    def __del__(self):
        Node._id -= 1


def tree1():
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    G = Node('G')
    H = Node('H')

    A.left = B
    A.right = C

    B.left = D

    C.left = E
    C.right = F

    E.left = G
    E.right = H

    return A, B, C, D, E, F, G, H


def tree2():
    A = Node('Alice')
    B = Node('Bob')
    C = Node('Caroline')
    D = Node('Darya')
    E = Node('Eve')
    F = Node('Fred')
    G = Node('Gonzalo')
    H = Node('Hadassah')

    A.left = B
    A.right = C

    B.left = D

    C.left = E
    C.right = F

    E.left = G
    E.right = H

    return A, B, C, D, E, F, G, H


