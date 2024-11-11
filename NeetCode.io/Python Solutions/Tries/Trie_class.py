import json

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
    def to_dict(self, node=None):
        if node is None:
            node = self.root
        
        node_dict = {}
        for char, child in node.children.items():
            node_dict[char] = self.to_dict(child)
        
        if node.endOfWord:
            node_dict["*"] = True
        
        return node_dict

    def to_json(self):
        with open('trie.json', 'w') as f:
            json.dump(self.to_dict(), f, indent=2)