N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]
result = []
idx = 0

for i in range(N):
    idx = (idx + K - 1) % len(arr)

    result.append(str(arr.pop(idx)))

print("<", ", ".join(result)[:], ">", sep = '')