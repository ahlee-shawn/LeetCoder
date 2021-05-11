# Sliding Window

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = left = sum(cardPoints[:k])
        right = 0
        left_index, right_index = k-1, len(cardPoints)-1
        for _ in range(k):
            left -= cardPoints[left_index]
            right += cardPoints[right_index]
            ans = max(ans, left+right)
            left_index -= 1
            right_index -= 1
        return ans