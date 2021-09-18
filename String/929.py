class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        table = dict()
        for email in emails: #O(n)
            emailSplitted = email.split('@')
            domainName = emailSplitted[1]
            localName = emailSplitted[0]
            realLocalName = ""
            for i in range(len(localName)):
                if localName[i] == '+':
                    break
                elif localName[i] != '.':
                    realLocalName += localName[i]
            if domainName not in table:
                table[domainName] = set()
            if realLocalName not in table[domainName]:
                table[domainName].add(realLocalName)
        ans = 0
        for key in table: #O(n)
            ans += len(table[key])
        return ans

