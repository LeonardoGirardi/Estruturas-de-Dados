"""Crie um programa que use uma
pilha para verificar se uma string é um  palíndromo.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None
        val = self.top.val
        self.top = self.top.next
        return val

def is_palindrome(word):
    stack = Stack()

    for letter in word:
        stack.push(letter)

    for letter in word:
        if letter != stack.pop():
            return False
    return True

string = "renner"
print(f"Is the word '{string}' a palindrome? {is_palindrome(string)}")


