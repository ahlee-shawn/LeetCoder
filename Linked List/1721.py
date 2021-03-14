# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        arr = []
        current = head
        while True:
            arr.append(current.val)
            current = current.next
            if current == None:
                break
        arr[k-1], arr[len(arr)-k] = arr[len(arr)-k], arr[k-1]
        current = head
        count = 0
        while True:
            current.val = arr[count]
            current = current.next
            if current == None:
                break
            count += 1
        return head