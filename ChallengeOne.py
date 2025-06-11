class TrieNode:
    def __init__(self):
        self.children = {}  
        self.is_end_of_word = False  

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True  

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

trie = Trie()


outputs = [None]
trie.insert("apple")                  
outputs.append(None)
outputs.append(trie.search("apple")) 
outputs.append(trie.search("app"))   
outputs.append(trie.startsWith("app")) 
trie.insert("app")                   
outputs.append(None)
outputs.append(trie.search("app"))   

print(outputs)  
