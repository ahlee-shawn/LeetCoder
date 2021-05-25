class Solution:
    
    def modifyArr(self, chars, index, nextIndex, countList):
        countListLength = len(countList)
        for i in range(index, index+countListLength):
            chars[i] = countList[i-index]
        for i in range(index+countListLength, nextIndex):
            chars.pop(index+countListLength)
        
    def compress(self, chars: List[str]) -> int:
        index = ans = 0
        while index < len(chars):
            nextIndex = index
            count = 0
            while nextIndex < len(chars) and chars[index] == chars[nextIndex]:
                count += 1
                nextIndex += 1
            if count == 1:
                ans += 1
                index += 1
            else:
                countList = list(str(count))
                self.modifyArr(chars, index+1, nextIndex, countList)
                ans += (len(countList) + 1)
                index += (len(countList) + 1)
        return ans