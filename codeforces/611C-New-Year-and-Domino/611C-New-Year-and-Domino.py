h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]

H = [[0]*(w+1) for _ in range(h+1)]
V = [[0]*(w+1) for _ in range(h+1)]

for i in range(h):
    for j in range(w):
        if j+1 < w and grid[i][j]=='.' and grid[i][j+1]=='.':
            H[i+1][j+1] = 1
        if i+1 < h and grid[i][j]=='.' and grid[i+1][j]=='.':
            V[i+1][j+1] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        H[i][j] += H[i-1][j] + H[i][j-1] - H[i-1][j-1]
        V[i][j] += V[i-1][j] + V[i][j-1] - V[i-1][j-1]

q = int(input())

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())

    h_ans = 0
    if c2 > c1:
        h_ans = H[r2][c2-1] - H[r1-1][c2-1] - H[r2][c1-1] + H[r1-1][c1-1]

    v_ans = 0
    if r2 > r1:
        v_ans = V[r2-1][c2] - V[r1-1][c2] - V[r2-1][c1-1] + V[r1-1][c1-1]

    print(h_ans + v_ans)