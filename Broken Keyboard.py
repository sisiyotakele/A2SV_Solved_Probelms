t = int(input())

for _ in range(t):
    s = input().strip()
    i = 0
    working = set()

    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1

        if count % 2 == 1:
            working.add(s[i])

        i += 1

    print("".join(sorted(working)))
