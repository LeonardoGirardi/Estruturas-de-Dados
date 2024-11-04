"""Utilize  a  estrutura  do  exercício  anterior  e  implemente  um
    método  para  impressão  dos nós em ordem crescente"""

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

bst.inorder(bst.root)








        



