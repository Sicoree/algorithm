N, K = map(int, input().split())
arr = list(map(int, input().split()))

tmp = 0
for i in range(K):
    tmp += arr[i]
result = tmp

for i in range(N - K):
    tmp -= arr[i]
    tmp += arr[i + K]

    if result < tmp:
        result = tmp

print(result)