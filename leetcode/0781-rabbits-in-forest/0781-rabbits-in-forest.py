class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = Counter(answers)
        count = 0
        for i,v in res.items():
            group = ceil (v/(i+1) )
            rab = group * (i+1)
            count += rab
        return count
        #     if  i == 0:
        #         count += v
        #     elif i == 1:
        #         if v %2 == 0:
        #             count += v
        #         else:
        #             count += v+1
        #     else:
        #         count += i+1
        # return count