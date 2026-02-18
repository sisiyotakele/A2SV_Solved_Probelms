t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pref = 0
    t1 = -1
    for i in range(n):
        if s[i] == 'L':
            pref -= 1
        else:
            pref += 1
        
        if x + pref == 0:
            t1 = i + 1
            break
    
    if t1 == -1 or t1 > k:
        print(0)
        continue
    ans = 1
    k -= t1
    pref = 0
    t2 = -1
    
    for i in range(n):
        if s[i] == 'L':
            pref -= 1
        else:
            pref += 1
        
        if pref == 0:
            t2 = i + 1
            break
    
    if t2 == -1:
        print(ans)
    else:
        ans += k // t2
        print(ans)
