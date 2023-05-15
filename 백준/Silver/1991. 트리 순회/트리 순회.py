import sys
input = sys.stdin.readline

def MLR(i):
    mid.append(arr[i])
    if i * 2 < 2**10 and arr[i * 2]:
        MLR(i * 2)
    
    if i * 2 + 1< 2**10 and arr[i * 2 + 1]:
        MLR(i * 2 + 1)
    
def LMR(i):
    if i * 2 < 2**10 and arr[i * 2]:
        LMR(i * 2)

    left.append(arr[i])
    
    if i * 2 + 1< 2**10 and arr[i * 2 + 1]:
        LMR(i * 2 + 1)
    
def LRM(i):
    if i * 2 < 2**10 and arr[i * 2]:
        LRM(i * 2)        
    
    if i * 2 + 1< 2**10 and arr[i * 2 + 1]:
        LRM(i * 2 + 1)

    right.append(arr[i])

N = int(input())

arr = [0 for _ in range(2**10)]
arr[1] = 'A'
for _ in range(N):
    m, l ,r = map(str, input().split())

    idx = arr.index(m)
    if l != '.':
        arr[idx * 2] = l
    if r != '.':
        arr[idx * 2 + 1] = r

left = []
right = []
mid = []

MLR(1)
LMR(1)
LRM(1)

print(''.join(mid))
print(''.join(left))
print(''.join(right))