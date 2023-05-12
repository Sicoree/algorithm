def DFS(s):
    if len(r) == M:
        print(' '.join(map(str, r)))
        return
    
    for i in range(s, N):
        if not v[i]:
            v[i] = 1
            r.append(arr[i])
            DFS(i)
            v[i] = 0
            r.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
v = [0] * N

r = []
DFS(0)