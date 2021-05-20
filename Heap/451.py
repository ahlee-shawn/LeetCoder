class Solution:
    def frequencySort(self, s: str) -> str:
        table = {}
        for c in s:
            if c in table:
                table[c] += 1
            else:
                table[c] = 1
        pq = []
        for key in table:
            pq.append((-table[key], key))
        heapq.heapify(pq)
        ans = ''
        while pq:
            count, c = heapq.heappop(pq)
            for i in range(-count):
                ans += c
        return ans