from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS():

    q = deque()
    q.append([0, 0])
    v[0][0] = 0

    while q:
        cx, cy = q.popleft()   

        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]

            if 0 <= nx < N and 0 <= ny < M and v[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    q.appendleft([nx, ny])
                    v[nx][ny] = v[cx][cy]
                else:
                    q.append([nx, ny])
                    v[nx][ny] = v[cx][cy] + 1
                    
M, N = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

v = [[-1] * M for _ in range(N)]

BFS()
print(v[N - 1][M - 1])