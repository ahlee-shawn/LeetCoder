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