t  = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    M = arr[-1]
    ans = 0
    for k in range(n):
        i = 0
        j = k - 1

        while i < j:
            if arr[i] + arr[j] > arr[k] and arr[i] + arr[j] + arr[k] > M:
                ans += j - i
                j -= 1
            else:
                i += 1
    print(ans)