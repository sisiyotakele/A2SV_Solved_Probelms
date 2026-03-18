class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(l,r):
            if l >= r:
                return 
            s[l] , s[r]= s[r],s[l]
            rev(l+1,r-1)
        rev(0,len(s) - 1)
        # n= len(s)
        # index = n-1
        # for i in range (0,n//2):
        #     temp = s[i]
        #     s[i] = s[index]
        #     s[index] = temp

        #     index -= 1
