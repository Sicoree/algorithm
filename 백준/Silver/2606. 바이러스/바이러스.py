from collections import deque

N = int(input())
M = int(input())

arr = [0 for _ in range(N + 1)]
g_list = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    g_list[u].append(v)
    g_list[v].append(u)

q = deque()
q.append(1)
arr[1] = 1
while q:
    cx = q.popleft()

    for cy in g_list[cx]:
        if arr[cy] == 0:
            arr[cy] = 1
            q.append(cy)

print(arr.count(1) - 1)
