class Solution:
    def convert_vowels_to_a(self, word):
        vowel_list = ['e', 'i', 'o', 'u']
        return_word = ""
        for i in range(len(word)):
            if word[i] in vowel_list:
                return_word += 'a'
            else:
                return_word += word[i]
        return return_word
    
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        word_table = dict()
        for word in wordlist:
            if word.lower() in word_table:
                is_in = False
                for i in range(len(word_table[word.lower()])):
                    if word_table[word.lower()][i] == word:
                        is_in = True
                        break
                if not is_in:
                    word_table[word.lower()].append(word)
            else:
                word_table[word.lower()] = [word]
        print(word_table)
        
        vowel_table = dict()
        for word in wordlist:
            word_vowel_a = self.convert_vowels_to_a(word.lower())
            if word_vowel_a in vowel_table:
                is_in = False
                for i in range(len(vowel_table[word_vowel_a])):
                    if vowel_table[word_vowel_a][i] == word:
                        is_in = True
                        break
                if not is_in:
                    vowel_table[word_vowel_a].append(word)
            else:
                vowel_table[word_vowel_a] = [word]
        print(vowel_table)
        
        ans = []
        for query in queries:
            correct = ""
            if query.lower() in word_table:
                is_in = False
                for i in range(len(word_table[query.lower()])):
                    if word_table[query.lower()][i] == query:
                        ans.append(query)
                        is_in = True
                        break
                if not is_in:
                    ans.append(word_table[query.lower()][0])
            elif self.convert_vowels_to_a(query.lower()) in vowel_table:
                query_vowels_a = self.convert_vowels_to_a(query.lower())
                ans.append(vowel_table[query_vowels_a][0])
            else:
                ans.append("")
        return ans