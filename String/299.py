class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a = b = 0
        secretCount = [0 for _ in range(10)]
        guessCount = [0 for _ in range(10)]
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                secretCount[int(secret[i])] += 1
                guessCount[int(guess[i])] += 1
        for i in range(10):
            b += min(secretCount[i], guessCount[i])
        return str(a) + "A" + str(b) + "B"