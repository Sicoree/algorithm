import sys
input = sys.stdin.readline

def DFS():
    if len(result) >= M:
        print(' '.join(map(str, result)))
        return
    
    use_num = -1
    for idx in range(N):
        if use_num != arr[idx]:
            result.append(arr[idx])
            use_num = arr[idx]
            DFS()
            result.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = []
DFS()