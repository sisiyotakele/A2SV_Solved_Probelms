class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_costs = sorted(costs, reverse=True)
        ans = []
        i = 0
        for x, y in costs:
            ans.append((x-y, i))
            i += 1
        ans.sort()
        a= []
        b = []
        for i,j in ans:
            if len(a) < len(costs) //2:
                a.append(costs[j][0])
            else:
                b.append(costs[j][1])

        return sum(a) + sum(b)
        
