class Solution:    
    def findUnion(self, a, b):
        # code here
        # a.sort()
        # b.sort()
        # a_s=set(a)
        # b_s=set (b)
        # res= (list( a_s | b_s))
        # return res      #works perfectly
        return sorted(list(set(a) | set(b) ))
