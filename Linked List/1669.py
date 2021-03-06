# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        current = list1
        for i in range(b+1):
            if i == a - 1:
                temp = current.next
                current.next = list2
                current = temp
            elif i == b:
                temp = current.next
                current_list2 = list2
                while True:
                    if current_list2.next is None:
                        current_list2.next = temp
                        return list1
                    else:
                        current_list2 = current_list2.next
            else:
                current = current.next