class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sp=sorted(points , key = lambda x:x[1])
        print(sp)
        count = 1
        fs = sp[0][1]
        for i in range(1,len(points)):
            if points[i][0] > fs:
                count += 1
                fs = points[i][1]
        return count

        


           
