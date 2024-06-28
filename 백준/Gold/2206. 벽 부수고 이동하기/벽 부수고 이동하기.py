from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1

    while q:
        cx, cy, c = q.popleft()
        cnt = visited[cx][cy][c]
        
        if cx == N - 1 and cy == M - 1:
            return cnt
            break

        for idx in range(4):
            nx = cx + dx[idx]
            ny = cy + dy[idx]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and c == 0:
                    q.append([nx, ny, c + 1])
                    visited[nx][ny][c + 1] = cnt + 1
                elif arr[nx][ny] == 0 and not visited[nx][ny][c]:
                    q.append([nx, ny, c])
                    visited[nx][ny][c] = cnt + 1
    
    return -1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] 

print(BFS())