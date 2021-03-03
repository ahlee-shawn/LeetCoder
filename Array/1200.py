class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        ans = []
        arr.sort()
        min_diff = arr[1] - arr[0]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < min_diff:
                ans = ([[arr[i], arr[i+1]]])
                min_diff = arr[i+1] - arr[i]
            elif arr[i+1] - arr[i] == min_diff:
                ans.append([arr[i], arr[i+1]])
        return ans