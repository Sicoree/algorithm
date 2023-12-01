import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, cnt):
    global result
    if result < cnt:
        result = cnt
        
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < R and 0 <= ny < C and visited[arr[nx][ny]] == 0:
            # visited.append(arr[nx][ny])
            # dfs(nx, ny, cnt + 1)
            # visited.pop()
            visited[arr[nx][ny]] = 1
            dfs(nx, ny, cnt + 1)
            visited[arr[nx][ny]] = 0

R, C = map(int, input().split())
# arr = [list(input().rstrip()) for _ in range(R)]
# visited = []
# visited.append(arr[0][0])

# 아스키 코드로 바꿔준다고 함
arr = [list(map(lambda x : ord(x) - 65, input())) for _ in range(R)]
visited = [0] * 26
visited[arr[0][0]] = 1

result = 1
dfs(0, 0, result)

print(result)