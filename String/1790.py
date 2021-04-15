class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_char = []
        different_char_number = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if different_char_number > 2:
                    return False
                if not diff_char:
                    diff_char.append(s1[i])
                    diff_char.append(s2[i])
                else:
                    if diff_char[0] != s2[i] or diff_char[1] != s1[i]:
                        return False
                different_char_number += 1
        return different_char_number % 2 == 0