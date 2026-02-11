class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1= Counter(word1)
        word2 = Counter(word2)

        if word1 == word2:
            return True
        word1_val=dict(sorted(word1.items(),key=lambda item: item[1],reverse =True))
        word2_val=dict(sorted(word2.items(),key=lambda item: item[1],reverse =True))

        if set(word1_val.keys()) != set(word2_val.keys()):
            return False

        if list(word1_val.values()) == list(word2_val.values()):
            return True
        else:
            return False
        
         
        
