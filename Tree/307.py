# Segment Tree

class Node(object):
    def __init(self, start, end, total, left, right):
        self.start = start
        self.end = end
        self.total = total
        self.left = left
        self.right = right

class NumArray(object):

    def __init__(self, nums: List[int]):
        self.tree, _ = self.createTree(nums, 0, len(nums)-1)
        
    def createTree(self, nums, start, end):
        if start == end:
            newNode = Node()
            newNode.start = start
            newNode.end = end
            newNode.total = nums[start]
            newNode.left = None
            newNode.right = None
            return newNode, newNode.total
        else:
            mid = (start + end) // 2
            left, leftTotal = self.createTree(nums, start, mid)
            right, rightTotal = self.createTree(nums, mid+1, end)
            newNode = Node()
            newNode.start = start
            newNode.end = end
            newNode.total = leftTotal + rightTotal
            newNode.left = left
            newNode.right = right
            return newNode, newNode.total

    def update(self, index: int, val: int) -> None:
        diff = self.updateDFS(index, val, self.tree)
    
    def updateDFS(self, index, val, node):
        if index == node.start == node.end:
            diff = val - node.total
            node.total = val
        else:
            mid = (node.start + node.end) // 2
            if index <= mid:
                diff = self.updateDFS(index, val, node.left)
            else:
                diff = self.updateDFS(index, val, node.right)
            node.total += diff
        return diff

    def sumRange(self, left: int, right: int) -> int:
        return self.sumRangeDFS(self.tree, left, right)
    
    def sumRangeDFS(self, node, left, right):
        if node.start == left and node.end == right:
            return node.total
        else:
            mid = (node.start + node.end) // 2
            if mid >= right:
                return self.sumRangeDFS(node.left, left, right)
            elif mid < left:
                return self.sumRangeDFS(node.right, left, right)
            else:
                return self.sumRangeDFS(node.left, left, mid) + self.sumRangeDFS(node.right, mid+1, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)