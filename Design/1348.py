class TweetCounts:

    def __init__(self):
        self.tweetDict = {}

    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName in self.tweetDict:
            self.tweetDict[tweetName].append(time)
        else:
            self.tweetDict[tweetName] = [time]

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.tweetDict:
            return []
        hop = 0
        if freq == "minute":
            hop = 60
        if freq == "hour":
            hop = 60 * 60
        if freq == "day":
            hop = 24 * 60 * 60

        timeList = self.tweetDict[tweetName] # [0, 60, 10]
        timeList.sort() # [0, 10, 60]
        
        index = 0 # index for timeList
        ans = []
        
        for i in range(((endTime - startTime) // hop) + 1):
            curSlotCount = 0
            s = startTime + hop * i # starting time in current time slot
            # fix the last time slot
            e = startTime + hop * i + (hop - 1) # ending time in current time slot
            if i == ((endTime - startTime) // hop) : # True when it's the last time slot
                e = min(e, endTime)
            # s = 0, e = 59
            while True:
                if index == len(timeList) or timeList[index] > e:
                    break
                if s <= timeList[index] <= e:
                    curSlotCount += 1
                    index += 1
                elif timeList[index] < s:
                    index += 1
            ans.append(curSlotCount)
        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)