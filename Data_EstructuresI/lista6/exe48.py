"""Crie  uma  arvore  binária  que  represente  uma  expressão  aritmética.
Instancie  as seguintes expressões e imprima a árvore em ordem.
a) 2 * (a – b / c);
b) a + b + 5 * c. """

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=' ')
            self.inorder(node.right)

bt = BinaryTree()
bt1 = BinaryTree()

# Expressao 1: 2*(a-b/c)

bt.root = Node("-")
bt.root.left = Node("(")
bt.root.right = Node("/")

bt.root.left.left = Node("*")
bt.root.left.right = Node("a")
bt.root.left.left.left = Node("2")

bt.root.right.left = Node("b")
bt.root.right.right = Node(")")
bt.root.right.right.left = Node("c")

bt.inorder(bt.root)
print()

# Expressao 2: a + b + 5 * c

bt1.root = Node("+")
bt1.root.left = Node("+")
bt1.root.right = Node("*")

bt1.root.left.left = Node("a")
bt1.root.left.right = Node("b")

bt1.root.right.left = Node("5")
bt1.root.right.right = Node("c")

bt1.inorder(bt1.root)