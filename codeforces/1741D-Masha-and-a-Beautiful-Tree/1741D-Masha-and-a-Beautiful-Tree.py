def solve(arr):
    if len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_ops = solve(arr[:mid])
    right, right_ops = solve(arr[mid:])

    if left is None or right is None:
        return None, 0

    if max(left) < min(right):
        return left + right, left_ops + right_ops

    elif max(right) < min(left):
        return right + left, left_ops + right_ops + 1

    else:
        return None, 0
t = int(input())
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    res, ops = solve(arr)
    print(ops if res is not None else -1)