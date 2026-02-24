class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j  = len(skill) -1
        comp = skill[i] +skill[j]
        catg=[]
        for i in range (len(skill)//2):
            if  comp == skill[i] +skill[j]:
                catg.append(skill[i] * skill[j])
            else:
                return -1
            j -= 1 
        total = sum(catg)
        return total
