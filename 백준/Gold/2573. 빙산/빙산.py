from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = 1
    melt = []

    while q:
        cx, cy = q.popleft()
        cnt = 0

        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]

            if 0 <= nx < N and 0 <= ny < M and not v[nx][ny]:
                if arr[nx][ny] == 0:
                    cnt += 1
                else:
                    q.append((nx, ny))
                    v[nx][ny] = 1
        
        if cnt > 0:
            melt.append((cx, cy, cnt))

    for x, y, cnt in melt:
        arr[x][y] = max(0, arr[x][y] - cnt)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

ice = []
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            ice.append((i, j))
count = 0

while ice:
    v = [[0] * M for _ in range(N)]
    d = []
    count = 0

    for i, j in ice:
        if arr[i][j] and not v[i][j]:
            count += 1
            BFS(i, j)
        if arr[i][j] == 0:
            d.append((i, j))
    
    if count > 1:
        print(result)
        break

    ice = sorted(list(set(ice) - set(d)))
    result += 1

if count < 2:
    print(0)