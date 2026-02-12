class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col=[]
        res =[]
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                col.append(matrix[j][i])
        k = 0
        while k < len(col):
            res.append(col[k:k+len(matrix)])
            k += len(matrix)
        print(res)
        return res


            


            
