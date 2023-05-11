color = ['W', 'B']

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

min = 64

for n in range(N - 7):
    for m in range(M - 7):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if arr[n + i][m + j] != color[(n + i + m + j) % 2]:
                    cnt += 1
        
        if cnt < min:
            min = cnt

        cnt = 0

        for i in range(8):
            for j in range(8):
                if arr[n + i][m + j] != color[(n + i + m + j + 1) % 2]:
                    cnt += 1
        if cnt < min:
            min = cnt

print(min)