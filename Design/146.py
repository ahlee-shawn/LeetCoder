class Node:
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.table = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.table:
            cur = self.table[key][1]
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            self._addToFront(cur)
            return self.table[key][0]
        return -1
    
    def _addToFront(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            cur = self.table[key][1]
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            self._addToFront(cur)
            self.table[key] = (value, cur)
        else:
            newNode = Node(key, value, None, None)
            # add to first
            self._addToFront(newNode)

            if self.used == self.capacity: # remove last
                del self.table[self.tail.prev.key]
                victim = self.tail.prev
                self.tail.prev = self.tail.prev.prev
                victim.prev.next = self.tail
                del victim
            else:
                self.used += 1
            self.table[key] = (value, newNode)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)