# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        reverse = None
        while head:
            current = head
            head = head.next
            current.next = reverse
            reverse = current
        return reverse

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursive(self, reverse, head):
        if not head:
            return reverse
        head_next = head.next
        head.next = reverse
        reverse = head
        return self.recursive(reverse, head_next)
        
    def reverseList(self, head: ListNode) -> ListNode:
        return self.recursive(None, head)