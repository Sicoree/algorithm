def DFS():
    if len(r) == M:
        print(' '.join(map(str, r)))
        return
    
    for i in range(1, N + 1):
        r.append(i)
        DFS()
        r.pop()

N, M = map(int, input().split())
r = []
DFS()