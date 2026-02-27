n, s = map(int, input().split())
nums = list(map(int, input().split()))
left = 0 
unq ={}
count = 0
for i in range(n):
    if nums[i] not in unq:
        unq[nums[i]] = 1
    else:
        unq[nums[i]] += 1
    
    while len(unq) > s:
        unq[nums[left]] -= 1
        if unq[nums[left]] == 0:
            del unq[nums[left]]
        left += 1
    count += (i-left + 1)
print(count)
