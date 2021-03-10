class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        counter = 0
        prime_counter = [0] * len(primes)
        ans = [1]
        while counter < n:
            temp = [0] * len(primes)
            for i in range(len(primes)):
                temp[i] = ans[prime_counter[i]]*primes[i]
            ans.append(min(temp))
            for i in range(len(primes)):
                if ans[-1] == ans[prime_counter[i]]*primes[i]:
                    prime_counter[i] += 1
            
            counter += 1
        
        return ans[n-1]