class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        table = set()
        for word in words:
            code = ""
            for char in word:
                code += morse_code[ord(char)-ord('a')]
            if code not in table:
                table.add(code)
        return len(table)