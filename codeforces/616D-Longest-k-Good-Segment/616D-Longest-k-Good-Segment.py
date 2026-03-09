from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))

count = defaultdict(int)
l = 0
distinct = 0
max_len = 0
ans_l = ans_r = 0

for r in range(n):
    count[a[r]] += 1
    if count[a[r]] == 1:
        distinct += 1

    while distinct > k:
        count[a[l]] -= 1
        if count[a[l]] == 0:
            distinct -= 1
        l += 1

    if r - l + 1 > max_len:
        max_len = r - l + 1
        ans_l, ans_r = l, r

print(ans_l + 1, ans_r + 1)