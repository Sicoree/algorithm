def DFS(i):
    if len(result) >= M:
        print(' '.join(map(str, result)))
        return

    v = 0
    for idx in range(i, N):
        if v != arr[idx]:
            result.append(arr[idx])
            v = arr[idx]
            DFS(idx + 1)
            result.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
v = [0] * N
DFS(0)