class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        dictionary ={}
        for i in responses:
            i =set(i)
            for j in i:
                if j in  dictionary:
                    dictionary[j] += 1
                else:
                    dictionary[j] = 1
        sorted_dict = dict(sorted(dictionary.items(), key=lambda item: (-item[1], item[0])))
        res = list(sorted_dict.keys())[0] 
        return res       
        
        
