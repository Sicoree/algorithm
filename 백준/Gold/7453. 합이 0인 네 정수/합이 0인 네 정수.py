n = int(input())
arr = [0 for _ in range(n)]
brr = [0 for _ in range(n)]
crr = [0 for _ in range(n)]
drr = [0 for _ in range(n)]

for idx in range(n):
    a, b, c, d = map(int, input().split())
    arr[idx] = a
    brr[idx] = b
    crr[idx] = c
    drr[idx] = d

sum_ab = dict()
for a in arr:
    for b in brr:
        s = a + b
        if s not in sum_ab.keys():
            sum_ab[s] = 1
        else:
            sum_ab[s] += 1

result = 0
for c in crr:
    for d in drr:
        s = -1 * (c + d)
        if s in sum_ab.keys():
            result += sum_ab[s]

print(result)