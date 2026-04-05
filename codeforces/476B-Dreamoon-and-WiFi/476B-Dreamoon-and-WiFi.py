from collections import Counter
import math
s1 = input().strip()
s2 = input().strip()

target = s1.count ("+") - s1.count("-")
cur = s2.count("+") - s2.count("-")
q = s2.count("?")

diff = target - cur
if (diff + q) %2 != 0:
    print(0.0)
    exit()
x = (diff + q) // 2 
if x < 0 or x > q:
    print(0.0)
    exit()
ways = math.comb(q,x)
tot = 2 ** q
print(ways/ tot)