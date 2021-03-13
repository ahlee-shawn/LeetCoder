class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        arr_dict = dict.fromkeys(arr, 1)
        def dp(num, arr_dict):
            for i in arr_dict:
                result = 0
                if num % i == 0 and (num // i in arr_dict):
                    if i in arr_dict:
                        result += arr_dict[i]*arr_dict[num//i]
                    else:
                        result += dp(i)*dp(num//i)
                    arr_dict[num] += result
            return arr_dict[num], arr_dict
        answer = 0
        for num in arr:
            result, arr_dict = dp(num, arr_dict)
            answer += result
        return answer % (10**9 + 7)