import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def DFS(x, y):
    
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < N and 0 <= ny < M and not arr[nx][ny]:
            arr[nx][ny] = 1
            result[-1] += 1
            DFS(nx, ny)

    return

M, N, K = map(int, input().split())
arr = [[0] * (M) for _ in range(N)]

for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            if not arr[i][j]:
                arr[i][j] = 1

cnt = 0
result = []

for i in range(N):
    for j in range(M):
        if not arr[i][j]:
            arr[i][j] = 1
            result.append(1)
            DFS(i, j)
            cnt += 1

print(cnt)
print(*sorted(result))