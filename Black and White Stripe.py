t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    s=list(s)
    b = s[:k].count('B')
    ans = k - b  
    for i in range(k,n):
        if s[i-k] == "B":
            b -= 1
        if s[i] == "B":
            b += 1
        
        mod = k - b

        if mod < ans:
            ans = mod

    print(ans)
