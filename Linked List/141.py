# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Set
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        table = set()
        current_node = head
        while current_node:
            if current_node not in table:
                table.add(current_node)
            else:
                return True
            current_node = current_node.next
        return False

# Two Pointers
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False