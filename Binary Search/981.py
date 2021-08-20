class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.table:
            self.table[key] = []
        self.table[key].append([timestamp, value])

    def binarySearch(self, array, target):
        low, mid, high = 0, 0, len(array)-1
        if array[low][0] > target:
            return ""
        if array[high][0] < target:
            return array[high][1]
        while low <= high:
            mid = low + ((high - low) // 2)
            if array[mid][0] == target:
                return array[mid][1]
            elif array[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
        return array[high][1]
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        else:
            return self.binarySearch(self.table[key], timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)