class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n < 3:
            return 1
        mod_n = 10**9 + 7
        prime_list = [i for i in range(3, n+1, 2)]
        prime_list.insert(0, 2)
        i = 1
        while True:
            current_prime = prime_list[i]
            for j in range(len(prime_list)-1, i, -1):
                if prime_list[j] % current_prime == 0:
                    prime_list.pop(j)
            i += 1
            if i >= len(prime_list):
                break
        prime = len(prime_list)
        not_prime = n - prime
        ans = 1
        for i in range(2, min(prime, not_prime)+1):
            ans *= i
            if ans > mod_n:
                ans %= mod_n
        ans = ((ans * ans) % mod_n)
        for i in range(min(prime, not_prime)+1, max(prime, not_prime)+1):
            ans *= i
            if ans > mod_n:
                ans %= mod_n
        return ans