def DFS():
    if len(result) >= M:
        print(' '.join(map(str, result)))
        return
    
    for idx in range(N):
        result.append(arr[idx])
        DFS()
        result.pop()
    

N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

result = []
DFS()