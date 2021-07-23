class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxValue = releaseTimes[0]
        maxKey = keysPressed[0]
        for i in range(1, len(releaseTimes)):
            tempValue = releaseTimes[i] - releaseTimes[i-1]
            if tempValue > maxValue:
                maxValue = tempValue
                maxKey = keysPressed[i]
            elif tempValue == maxValue and ord(keysPressed[i]) > ord(maxKey):
                maxKey = keysPressed[i]
        return maxKey
