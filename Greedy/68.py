class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        index = 0
        while index < len(words):
            curLine = ""
            count = 0
            length = 0
            while index + count < len(words):
                length += len(words[index + count])
                if length + count > maxWidth:
                    length -= len(words[index + count])
                    break
                count += 1
            if index + count < len(words):
                if count > 1:
                    spaceList = [0 for _ in range(count)]
                    space = maxWidth - length
                    spaceAvg = space // (count - 1)
                    spaceleft = space - (spaceAvg * (count - 1))
                    for i in range(len(spaceList)-1):
                        spaceList[i] = spaceAvg
                        if i < spaceleft:
                            spaceList[i] += 1
                    for i in range(count):
                        curLine += words[index + i]
                        for j in range(spaceList[i]):
                            curLine += " "
                else:
                    curLine += words[index]
                    for i in range(maxWidth - len(curLine)):
                        curLine += " "
            else:
                for i in range(index, len(words)-1):
                    curLine += (words[i] + " ")
                curLine += words[-1]
                for i in range(maxWidth - len(curLine)):
                    curLine += " "
            index += count
            ans.append(curLine)
        return ans