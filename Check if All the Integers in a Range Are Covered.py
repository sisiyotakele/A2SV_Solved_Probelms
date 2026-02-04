class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # for i in ranges:
        #     for j in range(i[0],i[1]+1):
        #         if j == left or j == right :
        #             return True    
        #     return False
        for i in range(left , right + 1):
            for s,e in ranges:
                if s <= i <= e:
                    break
            else:
                return False
        return True


