class Solution:
	def countSubstrings(self, s: str) -> int:
		if len(s) < 2:
			return len(s)
		
		n = len(s)
		table = [[False] * n for _ in range(n)]
		# palindromic string with length = 1
		for i in range(n):
			table[i][i] = True

		# palindromic string with length = 2
		for i in range(n-1):
			if s[i] == s[i+1]:
				table[i][i+1] = True

		# palindromic string with length > 2
		for j in range(n):
			for i in range(j):
				if table[i+1][j-1] and s[i] == s[j]:
					table[i][j] = True

		ans = 0
		for i in range(n):
			for j in range(i,n):
				if table[i][j]:
					ans += 1

		return ans