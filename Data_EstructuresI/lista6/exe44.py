"""Crie  uma  estrutura  que  represente  uma  árvore  binária.  Implemente  um  método  para inserção  de  nós:  
insira  10  valores  na  árvore  (pode  inserir  na  ordem  que  mantenha  a árvore balanceada) . """


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

    def inorder_traversal(self):
        self.inorder_recursive(self.root)

    def inorder_recursive(self, node):
        if node:
            self.inorder_recursive(node.left)
            print(node.data, end=' ')
            self.inorder_recursive(node.right)


bst = BinarySearchTree()

bst.insert(50)
bst.insert(30)
bst.insert(40)
bst.insert(55)
bst.insert(89)
bst.insert(65)
bst.insert(13)

bst.inorder_traversal()



