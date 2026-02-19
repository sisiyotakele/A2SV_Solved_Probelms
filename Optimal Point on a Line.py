n = int(input())
arr = list(map(int,input().split()))
arr.sort()
n = len(arr)
arr.sort()
if n % 2 == 1:
    mid = arr[n//2]
else:
    mid = arr[n//2 - 1]
print(mid)
