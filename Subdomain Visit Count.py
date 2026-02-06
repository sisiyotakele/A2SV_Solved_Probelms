class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cnt = Counter()

        for s in cpdomains:
            visits, domain = s.split()
            visits = int(visits)

            parts = domain.split('.')
            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                cnt[subdomain] += visits

        return [f"{v} {k}" for k, v in cnt.items()]
        
