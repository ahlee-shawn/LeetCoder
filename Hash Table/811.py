class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = []
        table = {}
        for cpdomain in cpdomains: # O(n), n elements in cpdomains
            spilt_count = cpdomain.split(' ')# O(m), m = string length
            count, domain = int(split_count[0]), split_count[1]
            sub_domain = domain.split('.')# O(m), m = string length
            # google.mail.com
            # ["google", "mail", "com"]
            sub_domain_name = ""
            for i in range(1, len(sub_domain)+1): #O(3)  # .join(string)

                if i == 1:
                    sub_domain_name = sub_domain[-i]
                else:
                    sub_domain_name = sub_domain[-i] + '.' + sub_domain_name
                if sub_domain_name not in table:
                    table[sub_domain_name] = count
                else:
                    table[sub_domain_name] += count
        for key in table: O(n), O(3n)
            ans.append(str(table[key]) + ' ' + key)
        return ans