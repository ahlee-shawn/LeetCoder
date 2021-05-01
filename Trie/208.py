class TrieNode:
    def __init__(self):
        self.isWord = False
        self.next = dict()

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_node = self.root
        for i in range(len(word)):
            if word[i] not in current_node.next:
                current_node.next[word[i]] = TrieNode()
            current_node = current_node.next[word[i]]
        current_node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_node = self.root
        for i in range(len(word)):
            if word[i] not in current_node.next:
                return False
            current_node = current_node.next[word[i]]
        return current_node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_node = self.root
        for i in range(len(prefix)):
            if prefix[i] not in current_node.next:
                return False
            current_node = current_node.next[prefix[i]]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)