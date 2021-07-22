class Node:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mod = 1000
        self.table = [None for _ in range(self.mod)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if self.table[key % self.mod] is None:
            newNode = Node()
            newNode.key = key
            newNode.val = value
            self.table[key % self.mod] = newNode
        else:
            curNode = self.table[key % self.mod]
            while curNode:
                if curNode.key == key:
                    curNode.val = value
                    return
                curNode = curNode.next
            newNode = Node()
            newNode.key = key
            newNode.val = value
            newNode.next = self.table[key % self.mod]
            self.table[key % self.mod] = newNode

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.table[key % self.mod] is None:
            return -1
        else:
            curNode = self.table[key % self.mod]
            while curNode:
                if curNode.key == key:
                    return curNode.val
                curNode = curNode.next
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if self.table[key % self.mod] is not None:
            curNode = self.table[key % self.mod]
            if curNode.key == key:
                self.table[key % self.mod] = curNode.next
                return
            prevNode = curNode
            curNode = curNode.next
            while curNode:
                if curNode.key == key:
                    prevNode.next = curNode.next
                prevNode = curNode
                curNode = curNode.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [[] for i in range(257)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        position = (key * 29 + 7) % 257
        if self.table[position] == []:
            self.table[position].append([key, value])
            return
        
        for i in range(len(self.table[position])):
            if self.table[position][i][0] == key:
                self.table[position][i][1] = value
                return
        self.table[position].append([key, value])
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        position = (key * 29 + 7) % 257
        
        for i in range(len(self.table[position])):
            if self.table[position][i][0] == key:
                return self.table[position][i][1]
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        position = (key * 29 + 7) % 257
        if len(self.table[position]) != 0:
            for i in range(len(self.table[position])):
                if self.table[position][i][0] == key:
                    self.table[position].pop(i)
                    return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)