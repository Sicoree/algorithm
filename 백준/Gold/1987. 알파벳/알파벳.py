dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(cx, cy, cnt):
    global result
    if result < cnt:
        result = cnt 

    for idx in range(4):
        nx = cx + dx[idx]
        ny = cy + dy[idx]

        if 0 <= nx < N and 0 <= ny < M and visited[arr[nx][ny]] == 0:
            visited[arr[nx][ny]] = 1
            DFS(nx, ny, cnt + 1)
            visited[arr[nx][ny]] = 0

N, M = map(int, input().split())
# 아스키 코드로 바꿔준다고 함
arr = [list(map(lambda x : ord(x) - 65, input())) for _ in range(N)]
visited = [0] * 26
visited[arr[0][0]] = 1

result = 0

DFS(0, 0, 1)
print(result)