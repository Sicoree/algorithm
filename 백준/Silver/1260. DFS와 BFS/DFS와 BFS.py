from collections import deque

def DFS(x):
    DFS_result.append(x)
    
    for y in range(N + 1):
        if g[x][y] == 1 and y not in DFS_result:
            DFS(y)

    return

def BFS(s):
    q = deque()
    q.append(s)
    BFS_result.append(s)

    while q:
        cx = q.popleft()

        for cy in range(N + 1):
            if g[cx][cy] == 1 and cy not in BFS_result:
                q.append(cy)
                BFS_result.append(cy)

N, M, V = map(int, input().split())

g = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    g[u][v] = 1
    g[v][u] = 1

DFS_result = []
BFS_result = []

DFS(V)
BFS(V)

print(" ".join(map(str, DFS_result)))
print(" ".join(map(str, BFS_result)))