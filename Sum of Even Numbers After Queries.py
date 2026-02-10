k = sum(x for x in nums if x % 2 == 0)
        res = []
        
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                k -= nums[idx]
            nums[idx] += val
            
            if nums[idx] % 2 == 0:
                k += nums[idx]
                
            res.append(k)
            
        return res
