from collections import defaultdict

t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    left_socks = defaultdict(int)
    right_socks = defaultdict(int)
    for i in range(l):
        left_socks[arr[i]] += 1
    for i in range(l, n):
        right_socks[arr[i]] += 1
        
    for color in list(left_socks.keys()):
        if color in right_socks:
            
            matches = min(left_socks[color], right_socks[color])
            left_socks[color] -= matches
            right_socks[color] -= matches
         
    left_count = sum(left_socks.values())
    right_count = sum(right_socks.values())
    
    if left_count < right_count:
        left_socks, right_socks = right_socks, left_socks
        left_count, right_count = right_count, left_count
        
    shifts_needed = (left_count - right_count) // 2
    ans = 0
    
    for color, count in left_socks.items():
        if shifts_needed == 0:
            break  
        possible_pairs = count // 2
        shifts_to_do = min(shifts_needed, possible_pairs)
        
        ans += shifts_to_do   
        shifts_needed -= shifts_to_do  
        left_count -= 2 * shifts_to_do 
    
    ans += left_count
    
    print(ans)