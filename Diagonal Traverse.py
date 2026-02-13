mapping = {}
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                s = r + c
                if s not in mapping:
                    mapping[s] = []
                mapping[s].append([r, c])
        
        res=[]
        for key,value in mapping.items():
            if key % 2 ==0:
                value.reverse()
            for n,m in  value:
                res.append(mat[n][m])
        return res
                
