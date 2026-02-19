n = int(input())
arr = list(map(int,input().split()))

arr.sort()
pos = 1
ans = 0
for i in arr:
    if i >= pos:
        pos += 1
    ans = pos-1
print(ans)

