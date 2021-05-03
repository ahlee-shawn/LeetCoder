class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans, low, high = 0, 0, len(people)-1
        while low <= high:
            if people[high] > limit:
                high -= 1
            elif people[low] + people[high] <= limit:
                ans += 1
                high -= 1
                low += 1
            else:
                ans += 1
                high -= 1
        return ans