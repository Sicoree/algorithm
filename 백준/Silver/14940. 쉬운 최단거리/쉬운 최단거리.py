import sys
from collections import deque
# input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def find_2():
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                return [i, j]

def BFS(x, y):
    q = deque()
    q.append([x, y])
    v[x][y] = 1

    while q:
        cx, cy = q.popleft()
        cw = result[cx][cy]

        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not v[nx][ny]:
                q.append([nx, ny])
                v[nx][ny] = 1
                result[nx][ny] = cw + 1

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * m for _ in range(n)]
v = [[0] * m for _ in range(n)]

x, y = find_2()
result[x][y] = 0
BFS(x, y)

for i in range(n):
    for j in range(m):
        if result[i][j] == 0 and arr[i][j] == 1:
            result[i][j] = -1

for i in range(n):
    print(*result[i])