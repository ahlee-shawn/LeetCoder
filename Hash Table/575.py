class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_categories = {}
        for candy in candyType:
            if candy not in candy_categories:
                candy_categories[candy] = 1
        
        return int(min(len(candy_categories), (len(candyType) / 2)))