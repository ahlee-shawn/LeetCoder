class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        ans = []
        odd = k % 2
        window = nums[:k]
        window.sort()
        if odd:
            ans.append(window[((k+1)//2)-1])
        else:
            ans.append((window[(k//2)-1] + window[(k//2)]) / 2)
        for i in range(len(nums)-k):
            window.remove(nums[i])
            bisect.insort(window, nums[i+k])
            if odd:
                ans.append(window[((k+1)//2)-1])
            else:
                ans.append((window[(k//2)-1] + window[(k//2)]) / 2)
        return ans