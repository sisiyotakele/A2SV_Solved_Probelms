def spruce():
    n = int(input())
    child = [[] for _ in range(n+1)]
    for node in range(2,n+1):
        par = int(input())
        child[par].append(node)

    for i in range(1,n+1):
        if len(child[i]) == 0:
            continue
        
        leaf_count = 0
        for ch in child[i]:
            if len(child[ch]) == 0:
                leaf_count += 1
        
        if leaf_count < 3:
            print("NO")
            return 
    print("YES")
spruce()