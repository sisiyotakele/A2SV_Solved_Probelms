from collections import Counter

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c_b = Counter(b)

i = 0
res = 0

while i < n:
    if a[i] in c_b:
        res += c_b[a[i]]
    i += 1

print(res)
