dx = [1, 0, -1 ,0]
dy = [0, 1, 0, -1]    

def solution(grid):
    answer = []
    arr = []
    for g in grid:
        arr.append(list(map(str, g)))
    
    M = len(arr)
    N = len(arr[0])
    
    
    v = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(M)]

    for i in range(M):
        for j in range(N):
            for idx in range(4):
                if v[i][j][idx] == 0:
                    cnt = 0
                    w = [i, j]
                    k = idx

                    while 1:
                        cx, cy = w
                        if v[cx][cy][k] == 0:
                            v[cx][cy][k] = 1
                        else:
                            answer.append(cnt)
                            break

                        nx = (cx + dx[k]) % M
                        ny = (cy + dy[k]) % N
                        if arr[nx][ny] == 'L':
                            k = (k + 1) % 4
                        elif arr[nx][ny] == 'R':
                            k = (k - 1) % 4

                        w = [nx, ny]
                        cnt += 1
    answer.sort()    
    return answer