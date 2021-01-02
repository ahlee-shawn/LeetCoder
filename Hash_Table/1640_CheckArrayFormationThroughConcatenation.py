class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        Dict = {}
        for i in pieces:
            Dict[i[0]] = i
        formedArray = []
        i = 0
        while(i < len(arr)):
            try:
                temp = Dict[arr[i]]
                for j in temp:
                    formedArray.append(j)
                i += len(temp)
            except KeyError:
                return False
        return formedArray == arr