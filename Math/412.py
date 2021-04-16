class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            current_ans = ""
            if i % 3 == 0:
                current_ans += "Fizz"
            if i % 5 == 0:
                current_ans += "Buzz"
            if current_ans == "":
                current_ans += str(i)
            ans.append(current_ans)
        return ans