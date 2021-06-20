# The Number of Full Rounds You Have Played
class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        startH = int(startTime[:2])
        startM = int(startTime[3:])
        start = startH * 60 + startM
        if start % 15:
            start = (int(start / 15) + 1) * 15
        endH = int(finishTime[:2])
        endM = int(finishTime[3:])
        end = endH * 60 + endM
        end = int(end / 15) * 15
        if end < start:
            end += (24*60)    
        return int((end - start) / 15)