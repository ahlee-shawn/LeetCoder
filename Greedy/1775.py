class Solution:
    def helper(self, sum1, table1, sum2, table2):
        diff = sum1 - sum2
        heap1, heap2 = [], []
        for i in range(1, 7):
            heapq.heappush(heap1, (-(i - 1), table1[i]))
            heapq.heappush(heap2, (-(6 - i), table2[i]))
        count = 0
        while heap1 and heap2:
            minus = heap1[0]
            add = heap2[0]
            if -minus[0] > -add[0]:
                minus = heapq.heappop(heap1)
                if -minus[0] * minus[1] > diff:
                    count += math.ceil(diff / -minus[0])
                    return count
                else:
                    count += minus[1]
                    diff -= -minus[0] * minus[1]
            else:
                add = heapq.heappop(heap2)
                if -add[0] * add[1] > abs(diff):
                    count += math.ceil(diff / -add[0])
                    return count
                else:
                    count += add[1]
                    diff -= -add[0] * add[1]
        print(heap1, heap2)
        print(count)
        if heap1:
            while heap1:
                minus = heapq.heappop(heap1)
                if -minus[0] * minus[1] > diff:
                    count += math.ceil(diff / -minus[0])
                    return count
                else:
                    count += minus[1]
                    diff -= -minus[0] * minus[1]
        elif heap2:
            while heap2:
                add = heapq.heappop(heap2)
                if -add[0] * add[1] > abs(diff):
                    count += math.ceil(diff / -add[0])
                    return count
                else:
                    count += add[1]
                    diff -= -add[0] * add[1]
        if diff > 0:
            return -1
        return count
        
        
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        table1 = defaultdict(int)
        table2 = defaultdict(int)
        sum1, sum2 = sum(nums1), sum(nums2)
        for num in nums1:
            table1[num] += 1
        for num in nums2:
            table2[num] += 1
        if sum1 > sum2:
            return self.helper(sum1, table1, sum2, table2)
        else:
            return self.helper(sum2, table2, sum1, table1)