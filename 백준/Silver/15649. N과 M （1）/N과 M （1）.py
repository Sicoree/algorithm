def solve(v, m, r):
    if m == M:
        print(' '.join(r))
        return
    
    for i in range(1, N + 1):
        if not v[i]:
            v[i] = 1
            r.append(str(i))
            solve(v, m + 1, r)
            v[i] = 0
            r.pop()

N, M = map(int, input().split())
arr = [n for n in range(N + 1)]

for idx in range(1, N + 1):
    vis = [0] * (N + 1)
    vis[idx] = 1
    res = [str(idx)]
    solve(vis, 1, res)