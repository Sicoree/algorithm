import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(s):
    global cnt
    
    for i in arr[s]:
        if not V[i]: 
            V[i] = cnt
            cnt += 1
            DFS(i)

N, M, R = map(int, input().split())

arr = [[] for _ in range(N + 1)]
V = [0 for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(1, N + 1):
    arr[i].sort()

cnt = 1
V[R] = cnt
cnt += 1
DFS(R)

for row in V[1:]:
    print(row)