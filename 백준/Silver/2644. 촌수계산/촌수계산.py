from collections import deque

def BFS():
    q = deque()
    q.append((x, 0))
    result.append(x)

    while q:
        u, c = q.popleft()

        if u == y:
            result.append(c)
            return

        for v in range(n + 1):
            if arr[u][v] == 1 and v not in result:
                result.append(v)
                q.append((v, c + 1))
    
    result.append(-1)

n = int(input())
x, y = map(int, input().split())
m = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
result = []

for _ in range(m):
    u, v = map(int, input().split())
    arr[u][v] = 1
    arr[v][u] = 1

BFS()

print(result[-1])