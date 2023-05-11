# 1854 / K변째 최단경로 찾기
# https://www.acmicpc.net/problem/1854
import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr =[[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

result = [[] for _ in range(n + 1)]
result[1].append(0)
q = [[0, 1]]

while q:
    cost, node = heapq.heappop(q)

    for next, w in arr[node]:
        dis = cost + w
        if len(result[next]) < k:
            heapq.heappush(result[next], -dis)
            heapq.heappush(q, [dis, next])
        elif dis < -result[next][0]:
            heapq.heappop(result[next])
            heapq.heappush(result[next], -dis)
            heapq.heappush(q, [dis, next])

for idx in range(1, n + 1):
    if len(result[idx]) < k:
        print(-1)
    else:
        print(-result[idx][0])
