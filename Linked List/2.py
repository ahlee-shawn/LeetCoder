# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode()
        cur = ans
        carry = 0
        while l1 and l2:
            value = l1.val+l2.val+carry
            if value > 9:
                carry = 1
                value -= 10
            else:
                carry = 0
            newNode = ListNode(value)
            cur.next = newNode
            cur = newNode
            l1 = l1.next
            l2 = l2.next
        if not l1 and not l2:
            if carry:
                newNode = ListNode(carry)
                cur.next = newNode
            return ans.next
        elif not l1:
            l1, l2 = l2, l1
        while l1:
            value = l1.val+carry
            if value > 9:
                carry = 1
                value -= 10
            else:
                carry = 0
            newNode = ListNode(value)
            cur.next = newNode
            cur = newNode
            l1 = l1.next
        if carry:
            newNode = ListNode(carry)
            cur.next = newNode
        return ans.next