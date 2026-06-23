class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        for word in queries:
            i = j = 0
            match = True

            while i < len(word):

                if j < len(pattern) and word[i] == pattern[j]:
                    i += 1
                    j += 1

                elif word[i].islower():
                    i += 1

                else:
                    match = False
                    break

            match = match and (j == len(pattern))
            ans.append(match)   
        return ans          
