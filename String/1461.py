class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        max_number = pow(2, k)
        visited_number = [False for _ in range(pow(2, k))]
        counter = 0
        for i in range(len(s)-k+1):
            temp = int(s[i:i+k], 2)
            if visited_number[temp] == False:
                visited_number[temp] = True
                counter += 1
            if counter == max_number:
                return True
        return False