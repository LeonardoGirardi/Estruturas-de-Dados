"""Crie  uma  estrutura  de  dados  Trie  e  implemente  a  funcionalidade  de  b
usca  de  uma palavra específica. """

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True


trie = Trie()

trie.insert("apple")
trie.insert("app")
trie.insert("applepie")
trie.insert("ape")
