import sys
input = sys.stdin.readline
 
N, D = map(int, input().split())
arr = [[] for _ in range(10001)]
for _ in range(N):
    s, e, w = map(int, input().split())
    arr[s].append([w, e])
distance = [i for i in range(D+1)]
 
for i in range(D+1):
    if i != 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    for w, e in arr[i]:
        if e <= D and distance[e] > w + distance[i]:
            distance[e] = w + distance[i]
 
print(distance[D])