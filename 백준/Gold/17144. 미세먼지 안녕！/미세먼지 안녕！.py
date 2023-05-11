R, C, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
t = 0

for i in range(R):
    if arr[i][0] == -1:
        n = i
        break

while t < T:
    arr_add = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5:
                cnt = 0
                for idx in range(4):
                    nx = i + dx[idx]
                    ny = j + dy[idx]
                    if 0 <= nx < R and 0 <= ny < C:
                        if arr[nx][ny] != -1:
                            arr_add[nx][ny] += arr[i][j] // 5
                            cnt += 1
                arr[i][j] -= (arr[i][j] // 5) * cnt  
    
    for i in range(R):
        for j in range(C):
            arr[i][j] += arr_add[i][j]

    for i in range(n - 1, 0, -1):
        arr[i][0] = arr[i - 1][0]    
    for i in range(0, C - 1):
        arr[0][i] = arr[0][i + 1]
    for i in range(0, n):
        arr[i][C - 1] = arr[i + 1][C - 1]
    for i in range(C - 1, 1, -1):
        arr[n][i] = arr[n][i - 1]
    arr[n][1] = 0

    for i in range(n + 2, R - 1):
        arr[i][0] = arr[i + 1][0]
    for i in range(0, C - 1):
        arr[R - 1][i] = arr[R - 1][i + 1]
    for i in range(R - 1, n + 1, -1):
        arr[i][C - 1] = arr[i - 1][C - 1]
    for i in range(C - 1, 1, -1):
        arr[n + 1][i] = arr[n + 1][i - 1]
    arr[n + 1][1] = 0

    t += 1

sum_arr = 2
for i in range(R):
    for j in range(C):
        sum_arr += arr[i][j]

print(sum_arr)