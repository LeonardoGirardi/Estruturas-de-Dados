"""Crie  uma  estrutura  que  represente  uma  árvore  binária  balanceada  e  implemente 
 a busca por um valor específico."""

class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        root = self.root
        while True:
            if data < root.data:
                if root.left:
                    root = root.left
                else:
                    root.left = Node(data)
                    return
            elif data > root.data:
                if root.right:
                    root = root.right
                else:
                    root.right = Node(data)
                    return
            else:
                return

    def in_order(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order(node.left, result)
            result.append(node.data)
            self.in_order(node.right, result)
        return result

bt = BinaryTree()

bt.insert(10)
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.insert(1)
bt.insert(15)

elements = bt.in_order(bt.root)
print(elements)




        




