class Node:
    def __init__(self):
        self.index = -1
        self.next = dict()

class WordFilter:
    
    def addPrefixSuffix(self, word):
        wordList = []
        wordList.append("#"+word)
        for i in range(1,len(word)+1):
            wordList.append(word[-i:]+"#"+word)
        return wordList

    def __init__(self, words: List[str]):
        self.root = Node()
        for i in range(len(words)):
            wordList = self.addPrefixSuffix(words[i])
            for word in wordList:
                currentNode = self.root
                for w in word:
                    if w not in currentNode.next:
                        currentNode.next[w] = Node()
                    currentNode = currentNode.next[w]
                    currentNode.index = i
        

    def f(self, prefix: str, suffix: str) -> int:
        target = suffix+"#"+prefix
        currentNode = self.root
        for i in range(len(target)):
            if target[i] not in currentNode.next:
                return -1
            else:
                currentNode = currentNode.next[target[i]]
        return currentNode.index


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)