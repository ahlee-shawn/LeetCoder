class Solution:
    def compare(self, words, table, index):
        # Return False if words[i] > words[i-1]
        word1 = words[index-1]
        word2 = words[index]
        for i in range(min(len(word1), len(word2))):
            order1 = table[ord(word1[i]) - ord('a')]
            order2 = table[ord(word2[i]) - ord('a')]
            if order2 < order1:
                return True
            elif order2 > order1:
                return False
        if len(word1) > len(word2):
            return False
        else:
            return True
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = [0 for _ in range(26)]
        value = 26
        for i in range(len(order)):
            table[ord(order[i]) - ord('a')] = value
            value -= 1
        for i in range(1, len(words)):
            if not self.compare(words, table, i):
                return False
        return True

class Solution:
    def create_order_table(self, order, table):
        for i in range(26):
            table[order[i]] = 26-i
        return table
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        table = self.create_order_table(order, {})
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            length = min(len(word1), len(word2))
            for j in range(length):
                if table[word1[j]] > table[word2[j]]:
                    break
                elif table[word1[j]] < table[word2[j]]:
                    return False
                else:
                    if j == length -1 and len(word1) > len(word2):
                        return False
        
        return True