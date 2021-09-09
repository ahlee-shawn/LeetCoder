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

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        forward = [0 for _ in range(n)]
        backward = [0 for _ in range(n)]
        temp = 0
        for i in range(k):
            temp += cardPoints[i]
            forward[i] = temp
        temp = 0
        for i in range(k):
            temp += cardPoints[n - 1 - i]
            backward[n - 1 - i] = temp
        ans = max(forward[k - 1], backward[n - k])
        left, right = 0, n - k + 1
        for i in range(k - 1):
            ans = max(ans, forward[left] + backward[right])
            left += 1
            right += 1
        return ans