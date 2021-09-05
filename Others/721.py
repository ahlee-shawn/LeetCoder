class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])
    
    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)
        if parentA != parentB:
            if parentA < parentB:
                self.parent[parentB] = parentA
            else:
                self.parent[parentA] = parentB
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = UnionFind(1000000)
        map_email_name = dict()
        map_email_id = dict()
        map_id_email = dict()
        id = 0
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email = account[i]
                map_email_name[email] = name
                if email not in map_email_id:
                    map_email_id[email] = id
                    map_id_email[id] = email
                    id += 1
                union.union(map_email_id[account[1]], map_email_id[email])
        
        merged_emails = defaultdict(set)
        for i in range(id):
            merged_emails[union.find(i)].add(map_id_email[i])
            
        ans = []
        for (id, emails) in merged_emails.items():
            name = map_email_name[map_id_email[id]]
            ans.append([name] + list(sorted(emails)))
        return ans