from collections import Counter
 
T = int(input())
for _ in range(T):
    s_str = input().strip()
    t_str = input().strip()
 
    s_count = Counter(s_str)
    t_count = Counter(t_str)
 
    possible = True
    for ch in s_count:
        if t_count[ch] < s_count[ch]:
            possible = False
            break
 
    if not possible:
        print("Impossible")
        continue
 
    rem = []
    for ch in t_count:
        extra = t_count[ch] - s_count[ch]
        if extra > 0:
            rem.extend([ch] * extra)
 
    rem.sort()
    i = 0
    j =0
    res = []
    while  i< len(s_str) and j < len(rem):
        if rem[j] < s_str[i]:
            res.append(rem[j])
            j += 1
        else:
            res.append(s_str[i])
            i += 1
    res.extend(s_str[i:])
    res.extend(rem[j:])
    print("".join(res))
