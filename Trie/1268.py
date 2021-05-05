# Trie
class Node:
    def __init__(self):
        self.isWord = False
        self.next = [None for _ in range(26)]
        
class Trie:
    def __init__(self):
        self.root = Node()
    
    def addWord(self, word):
        currentNode = self.root
        for char in word:
            if not currentNode.next[ord(char)-ord('a')]:
                newNode = Node()
                currentNode.next[ord(char)-ord('a')] = newNode
            currentNode = currentNode.next[ord(char)-ord('a')]
        currentNode.isWord = True
    
    def dfs(self, currentNode, wordStack, newSuggestions, remainingWords):
        if not remainingWords:
            return newSuggestions, remainingWords
        if currentNode.isWord:
            remainingWords -= 1
            temp = ""
            for word in wordStack:
                temp += word
            newSuggestions.append(temp)
        
        for i in range(26):
            nextNode = currentNode.next[i]
            if nextNode:
                wordStack.append(chr(i+ord('a')))
                newSuggestions, remainingWords = self.dfs(nextNode, wordStack, newSuggestions, remainingWords)
                wordStack.pop(-1)
        return newSuggestions, remainingWords
    
    def find3Words(self, currentRoot, wordStack):
        newSuggestions, remainingWords = self.dfs(currentRoot, wordStack, [], 3)
        return newSuggestions
            
    
    def suggest(self, searchWord):
        ans, wordStack = [], []
        currentRoot = self.root
        for word in searchWord:
            if currentRoot:
                currentRoot = currentRoot.next[ord(word)-ord('a')]
            if currentRoot:
                wordStack.append(word)
                newSuggestions = self.find3Words(currentRoot, wordStack)
            else:
                newSuggestions = ""
            ans.append(newSuggestions)
        return ans
    
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for word in products:
            trie.addWord(word)
        return trie.suggest(searchWord)

# Binary Search
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans, prefix, i = [], '', 0
        for char in searchWord:
            prefix += char
            i = bisect.bisect_left(products, prefix, lo=i, hi=len(products))
            ans.append([w for w in products[i:i + 3] if w.startswith(prefix)])
        return ans