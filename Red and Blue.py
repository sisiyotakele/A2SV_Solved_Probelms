t = int(input())
for _ in range(t):
    n = int(input())
    r =list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))
    pref_r = [0]*(len(r)+1)
    for i in range(len(r)):
        pref_r[i+1] = pref_r[i] + r[i]
    pref_b = [0]*(len(b)+1)
    for i in range(len(b)):
        pref_b[i+1] = pref_b[i] +b[i]
 
    ans = max(0,(max(pref_b) + max(pref_r)))
 
    print(ans)
