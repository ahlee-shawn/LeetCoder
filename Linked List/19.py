# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        slow_prev = None
        for _ in range(n-1):
            fast = fast.next
        print(fast.val)
        if not fast.next:
            return head.next
        while True:
            fast = fast.next
            slow_prev = slow
            slow = slow.next
            if not fast.next:
                break
        slow_prev.next = slow.next
        return head