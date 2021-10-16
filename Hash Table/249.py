class Solution:
    def groupStrings(self, strings):
        table = defaultdict(list)
        for i in range(len(strings)):
            first_char = strings[i][0]
            offset = ord(first_char) - ord('a')
            list_key = [0]
            for j in range(1, len(strings[i])):
                list_key.append((ord(strings[i][j]) - offset) % 26)
            tuple_key = tuple(list_key)
            table[tuple_key].append(strings[i])
        ans = []
        for key in table:
            ans.append(table[key])
        return ans