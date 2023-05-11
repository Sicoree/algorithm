# 13460|G1 / 구슬 탈출 2
# https://www.acmicpc.net/problem/13460

from collections import deque
import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(rx, ry, bx, by):

    q = deque()
    q.append([rx, ry, bx, by, 0])
    v = []
    v.append([rx, ry, bx, by])


    while q:
        crx, cry, cbx, cby, cnt = q.popleft()

        if cnt > 10:
            return -1
        if arr[crx][cry] == 'O':
            return cnt

        for idx in range(4):
            nrx, nry = crx, cry

            while 1:
                nrx += dx[idx]
                nry += dy[idx]
                if arr[nrx][nry] == '#':
                    nrx -= dx[idx]
                    nry -= dy[idx]
                    break
                elif arr[nrx][nry] == 'O':
                    break

            nbx, nby = cbx, cby
            while 1:
                nbx += dx[idx]
                nby += dy[idx]
                if arr[nbx][nby] == '#':
                    nbx -= dx[idx]
                    nby -= dy[idx]
                    break
                elif arr[nbx][nby] == 'O':
                    break     
            if arr[nbx][nby] == 'O':
                continue
            if nrx == nbx and nry == nby:
                if abs(nrx - crx) + abs(nry - cry) > abs(nbx - cbx) + abs(nby - cby):
                    nrx -= dx[idx]
                    nry -= dy[idx]
                else:
                    nbx -= dx[idx]
                    nby -= dy[idx]
            # if (nrx, nry, nbx, nby) not in v:
            q.append([nrx, nry, nbx, nby, cnt + 1])
                # v.append([nrx, nry, nbx, nby])
                
    return -1


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]


# 구멍, red, blue 찾기
for i in range(N):
    for j in range(M):
        if arr[i][j] != '.' and arr[i][j] != '#':
            if arr[i][j] == 'O':
                end = [i, j]
            # red
            elif arr[i][j] == 'R':
                rx = i
                ry = j
            # blue
            elif arr[i][j] == 'B':
                bx = i
                by = j

print(BFS(rx, ry, bx, by))