'''
BFS -> Too slow
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        level = 1
        visited_number = [[0]]
        while True:
            current_level = visited_number.pop(0)
            new_level = []
            for i in current_level:
                for j in coins:
                    temp = i + j
                    if temp == amount:
                        return level
                    new_level.append(temp)
            visited_number.append(new_level)
            level += 1
            print(level)
            if min(new_level) > amount:
                return -1
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        visited_number = [0] + [float('inf') for _ in range(amount)]
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    visited_number[i] = min(visited_number[i], visited_number[i-coin]+1)
        
        if visited_number[amount] == float('inf'):
            return -1
        else:
            return visited_number[amount]