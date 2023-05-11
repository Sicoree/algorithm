# 1707 / 이분 그래프
# https://www.acmicpc.net/problem/1707
import sys
from collections import deque

input = sys.stdin.readline

def BFS(s, graph):

    q = deque()
    q.append(s)
    v[s] = graph

    while q:

        x = q.popleft()

        for idx in arr[x]:
            if not v[idx]:
                q.append(idx)
                v[idx] = -1 * v[x]
            elif v[idx] == v[x]:
                return 0
    return 1

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())    

    arr = [[] for _ in range(V + 1)]
    v = [0] * (V + 1)

    for _ in range(E):
        x, y = map(int, input().split())

        arr[x].append(y)
        arr[y].append(x)
    
    for idx in range(1, V + 1):
        if not v[idx]:
            result = BFS(idx, 1)
            if not result:
                break
    
    print("YES" if result else "NO")