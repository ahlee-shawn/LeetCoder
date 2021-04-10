import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        stack = deque()
        current = head
        for _ in range(math.floor(length/2)):
            stack.append(current.val)
            current = current.next
        if length % 2:
            current = current.next
        for _ in range(math.ceil(length/2), length):
            if stack.pop() != current.val:
                print(stack)
                print(current.val)
                return False
            current = current.next
        return True

'''
Reverse Second Half of the Linked List -> Mush Faster
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = None
        while slow:
            current = slow
            slow = slow.next
            current.next = second_half
            second_half = current
        
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        return True