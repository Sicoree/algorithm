import sys
N, M, B = map(int,input().split())
block = []
for _ in range(N):
    block.append([int(x) for x in sys.stdin.readline().rstrip().split()])

ans = int(1e9)
h = 0

for i in range(257):
    iblock = 0
    bblock = 0
    for x in range(N):
        for y in range(M):
            if block[x][y] > i:
                bblock += block[x][y] - i
            else:
                iblock += i - block[x][y]

    if iblock > bblock + B:
        continue

    count = bblock * 2 + iblock

    if count <= ans:
        ans = count
        h = i

print(ans, h)