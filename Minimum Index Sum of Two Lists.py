class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = list (set (list1).intersection(set(list2)))
        if len (common) == 1:
            return common
        result={}
        for x in common :
            i=list1.index(x)
            j=list2.index(x)

            if (i+j) in result:
                result[i+j].append(x)
                print (result)
            else:
                result[i+j]=[x]
        return result[min(result.keys())]
