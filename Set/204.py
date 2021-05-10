class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = set()
        for i in range(2, int(sqrt(n))+1):
            if i not in primes:
                for multiple in range(i*i, n, i):
                    primes.add(multiple)
        return n - len(primes) - 2