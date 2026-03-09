t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    zeros = 0
    ones = 0
    balance = []
    for ch in a:
        if ch == '0':
            zeros += 1
        else:
            ones += 1
        balance.append(zeros - ones)  

    flip = 0
    possible = True
    for i in range(n-1, -1, -1):
        current = a[i]
        if flip:
            current = '0' if current == '1' else '1'
        if current != b[i]:
            if balance[i] != 0:
                possible = False
                break
            flip ^= 1  

    print("YES" if possible else "NO")