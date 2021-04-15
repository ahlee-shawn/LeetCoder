# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while True:
            ans = ans << 1 # ans *= 2
            ans = ans | head.val # ans += head.val
            head = head.next
            if not head:
                break
        return ans