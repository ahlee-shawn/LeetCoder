class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0 for _ in range(60)]
        for i in range(len(time)):
            arr[(time[i] % 60)] += 1
        ans = 0
        for i in range(1, 30):
            ans += (arr[i] * arr[60-i])
        ans += ((arr[0] * (arr[0]-1)) // 2)
        ans += ((arr[30] * (arr[30]-1)) // 2)
        return ans