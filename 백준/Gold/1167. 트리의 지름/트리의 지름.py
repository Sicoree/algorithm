import sys
from collections import deque
input = sys.stdin.readline

def BFS(s):
    v = [-1] * (V + 1)
    q = deque()
    q.append(s)
    v[s] = 0
    result = [0, 0]

    while q:
        cv = q.popleft()

        for u, w in g[cv]:
            if v[u] == -1:
                v[u] = v[cv] + w
                q.append(u)
                if result[0] < v[u]:
                    result = v[u], u
    
    return result

V = int(input())

g = [[] for _ in range(V + 1)]

for v in range(1, V + 1):
    arr = list(map(int, input().split()))

    for idx in range(1, len(arr) + 1, 2):
        if arr[idx] == -1:
            break
        
        g[arr[0]].append([arr[idx], arr[idx + 1]])

result, node = BFS(1)
result, node = BFS(node)

print(result)