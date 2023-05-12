N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = 0
e = arr[-1]
result = 0

while s < e:
    m = (s + e) // 2
    sum = 0

    for w in arr:
        if m < w:
            sum += w - m
            
    if sum == M:
        result = m
        break
    elif sum < M:
        e = m
    else:
        if result < m:
            result = m
            s = m + 1
        else:
            s = m + 1

print(result)