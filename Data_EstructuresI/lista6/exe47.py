"""Crie  uma  estrutura  que  represente  uma  árvore  binária  e  as
 implementações  dos métodos de impressão em ordem, pós-ordem e pré-ordem."""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_recursive(self.root, data)

    def insert_recursive(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_recursive(node.left, data)
        if data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_recursive(node.right, data)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')


bst = BinarySearchTree()

bst.insert(20)
bst.insert(10)
bst.insert(34)
bst.insert(15)
bst.insert(45)
bst.insert(12)
bst.insert(78)
bst.insert(17)
bst.insert(100)

print("In-order Tree: ")
bst.inorder(bst.root)
print()
print("Pre-order Tree: ")
bst.preorder(bst.root)
print()
print("Pos-order Tree: ")
bst.postorder(bst.root)

