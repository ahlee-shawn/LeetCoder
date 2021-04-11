class Solution:
    def toGoatLatin(self, S: str) -> str:
        ans = ""
        last_a = 'a'
        for word in S.split():
            if word[0] not in ('aAeEiIoOuU'):
                first = word[0]
                word = word[1:]
                word += first
            ans += (word + 'ma' + last_a + ' ')
            last_a += 'a'
        return ans[:-1]