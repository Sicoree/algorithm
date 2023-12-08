from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y):
    q = deque()
    q.append([x, y])
    v[x][y] = 1
    cnt = 1

    while q:
        cx, cy = q.popleft()
        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] and not v[nx][ny]:
                q.append([nx, ny])
                v[nx][ny] = 1
                cnt += 1
    
    return cnt

 

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0] * N for _ in range(N)]
result = 0
cnt_arr = []

for i in range(N):
    for j in range(N):
        if arr[i][j] and not v[i][j]:
            cnt_arr.append(BFS(i, j))
            result += 1

cnt_arr.sort()
print(result)
for cnt in cnt_arr:
    print(cnt)