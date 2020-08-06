class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.IsEnd = False

class Trie:
    def __init__(self):
        self.root=TrieNode(None)

    def insert(self,word):           #O(m)
        parent = self.root
        for i,char in enumerate(word):
            if char not in parent.children:
                parent.children[char] = TrieNode(char)
            parent = parent.children[char]
            if i == len(word)-1:
                parent.IsEnd = True

    def search(self,word):    #O(m)
        parent=self.root
        for char in word:
            if char not in parent.children:
                return False
            parent=parent.children[char]
        return parent.IsEnd

    def startsWith(self,prefix):
        parent=self.root
        for char in prefix:
            if char not in prefix:
                return False
            parent=parent.children[char]
        return True


ob1 = Trie()
ob1.insert("apple")
print(ob1.search("apple"))
print(ob1.search("app"))
print(ob1.startsWith("app"))
ob1.insert("app")
print(ob1.search("app"))