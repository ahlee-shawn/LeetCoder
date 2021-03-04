# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A, len_B = 0, 0
        A, B = headA, headB
        while A is not None:
            len_A += 1
            A = A.next
        while B is not None:
            len_B += 1
            B = B.next
            
        # headA is longer than headB
        if len_A < len_B:
            A, B = headB, headA
        else:
            A, B = headA, headB

        for i in range(abs(len_A-len_B)):
            A = A.next
        
        while True:
            if A == B:
                return A
            if A is None:
                return None
            A = A.next
            B = B.next