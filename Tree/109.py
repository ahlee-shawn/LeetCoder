# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convert(self, head):
        if not head:
            return None
        if not head.next:
            return TreeNode(val=head.val)
        slow, fast, pre = head, head, None
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        root = TreeNode(val=slow.val)
        root.left = self.convert(head)
        root.right = self.convert(slow.next)
        return root
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.convert(head)