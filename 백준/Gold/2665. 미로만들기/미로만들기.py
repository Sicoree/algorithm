from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS():
    q = deque()
    q.append([0, 0])
    v[0][0] = 1

    while q:
        cx, cy = q.popleft()
        cw = v[cx][cy]

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                if not arr[nx][ny]:
                    if not v[nx][ny]:
                        v[nx][ny] = cw + 1
                        q.append([nx, ny])
                    elif v[nx][ny] > cw + 1:
                        v[nx][ny] = cw + 1
                        q.append([nx, ny])
                else:
                    if not v[nx][ny]:
                        v[nx][ny] = cw
                        q.append([nx, ny])
                    elif v[nx][ny] > cw:
                        v[nx][ny] = cw
                        q.append([nx, ny])

    return

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
v = [[0] * n for _ in range(n)]

BFS()
print(v[n - 1][n - 1] - 1)