class Node:
    def __init__(self):
        self.isWord = False
        self.next = dict()

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        currentNode = self.root
        for i in range(len(word)):
            if word[i] not in currentNode.next:
                currentNode.next[word[i]] = Node()
            currentNode = currentNode.next[word[i]]
        currentNode.isWord = True
    
    def dfs(self, root, word, i):
        if i == len(word):
            return root.isWord
        if word[i] in root.next:
            return self.dfs(root.next[word[i]], word, i+1)
        partial_result = False
        if word[i] == '.':
            for key in root.next:
                partial_result = partial_result or self.dfs(root.next[key], word, i+1)
                if partial_result:
                    return True
            return False
        

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)