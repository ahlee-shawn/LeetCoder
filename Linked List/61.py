# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        list_length = 1
        last_node = head
        while last_node.next:
            list_length += 1
            last_node = last_node.next
        k %= list_length
        current_node = head
        for i in range(list_length-k-1):
            current_node = current_node.next
        last_node.next = head
        head = current_node.next
        current_node.next = None
        return head