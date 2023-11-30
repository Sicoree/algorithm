import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(cx, cy, s, cnt):
    global result
    if cnt >= 4:
        if result < s:
            result = s
        return
    
    for idx in range(4):
        nx = cx + dx[idx]
        ny = cy + dy[idx]

        if 0 <= nx < N and 0 <= ny < M and not v[nx][ny]:
            v[nx][ny] = 1
            DFS(nx, ny, s + arr[nx][ny], cnt + 1)
            v[nx][ny] = 0

def another(cx, cy):
    global result
    for t in range(4):
        s = arr[cx][cy]
        for k in range(3):
            idx = (t + k) % 4
            nx = cx + dx[idx]
            ny = cy + dy[idx]

            if not (0 <= nx < N and 0 <= ny < M):
                s = 0
                break
            s += arr[nx][ny]
        if result < s:
            result = s

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0] * M for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        v[i][j] = 1
        DFS(i, j, arr[i][j], 1)
        v[i][j] = 0

        another(i, j)
print(result)