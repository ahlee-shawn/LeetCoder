class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = set()
        for i in range(len(jewels)):
            table.add(jewels[i])
        answer = 0
        for i in range(len(stones)):
            if stones[i] in table:
                answer += 1
        return answer