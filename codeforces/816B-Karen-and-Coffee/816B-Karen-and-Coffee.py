n,k,q=map(int,input().split())
max_lm = 200000
diff = [0] * 200002
for _ in range(n):
    l,r  = map(int,input().split())
    diff[l] += 1
    diff[r+1] -= 1

count_arr = [0] * (max_lm + 2)
valid_arr = [0] * (max_lm +2)

for i in  range(1, max_lm  + 2):
    count_arr[i] = count_arr[i-1] + diff[i]

    if count_arr[i] >= k:
        valid_arr[i] = 1
    else:
        valid_arr[i] = 0
prefix_arr = [0] *(max_lm + 2)    
for i in range(1, max_lm+2):
    prefix_arr[i] = prefix_arr[i-1] + valid_arr[i]

for _ in range(q):
    a,b =map(int,input().split())
    ans = prefix_arr[b] - prefix_arr[a-1]

    print(ans)