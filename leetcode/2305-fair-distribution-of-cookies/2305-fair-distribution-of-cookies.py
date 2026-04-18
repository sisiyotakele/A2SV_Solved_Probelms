class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        distribution = [0] * k
        self.best = float('inf')

        def dfs(i):
            if i == n:
                self.best = min(self.best, max(distribution))
                return
            for j in range(k):
                if distribution[j] >= self.best:
                    continue
                
                distribution[j] += cookies[i]
                if max(distribution) < self.best:
                    dfs(i + 1)
                
                distribution[j] -= cookies[i]
                if distribution[j] == 0:
                    break

        dfs(0)
        return self.best