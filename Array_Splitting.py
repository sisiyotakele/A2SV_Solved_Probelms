n,k =list(map(int, input().split()))
arr = list(map(int, input().split()))
if k == 1:
    print(arr[-1] - arr[0])
    exit()
tot = arr[-1] - arr[0]
gap=[]
for i in range(len(arr) - 1):
    gap.append(arr[i+1] - arr[i])
gap.sort(reverse = True)
ans=tot- sum(gap[:k-1])
print(ans)
