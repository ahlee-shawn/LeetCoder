class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        queue = deque()
        queue.append(start)
        while queue:
            curIndex = queue.popleft()
            if curIndex not in visited:
                visited.add(curIndex)
                left = curIndex - arr[curIndex]
                right = curIndex + arr[curIndex]
                if left >= 0 and left not in visited:
                    queue.append(left)
                if right < len(arr) and right not in visited:
                    queue.append(right)
            if not arr[curIndex]:
                return True
        return False