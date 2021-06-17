"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        while True:
            newNode = Node(x=cur.val, next=cur.next, random=None)
            nextNode = cur.next
            cur.next = newNode
            if not nextNode:
                break
            else:
                cur = nextNode
        
        origin = head
        copy = head.next
        while True:
            if origin.random:
                copy.random = origin.random.next
            origin = origin.next.next
            if not origin:
                break
            copy = copy.next.next
        
        copy = head.next
        cur = copy
        while cur.next:
            nextNode = cur.next.next
            cur.next = cur.next.next
            cur = nextNode
        return copy