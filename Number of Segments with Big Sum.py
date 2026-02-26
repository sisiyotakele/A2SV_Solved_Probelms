n, s = map(int, input().split())
nums = list(map(int, input().split()))
left = 0 
curr_sum = 0
max_sum = 0 
for right in range(n):
    curr_sum += nums[right]
 
    while curr_sum >= s:
        max_sum  += (n-right)
        curr_sum -= nums[left]
        left += 1
    
print(max_sum)
