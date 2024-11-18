import sys


N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))

    if arr[0] == 1:
        stack.append(arr[1])
    elif arr[0] == 2:
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif arr[0] == 3:
        print(len(stack))
    elif arr[0] == 4:
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif arr[0] == 5:
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)