#  2042 / 구간 합 구하기
#  https://www.acmicpc.net/problem/2042
import sys
input = sys.stdin.readline

def init(node, left, right):
    if left == right:
        arr[node] = tmp[left]
        return arr[node]
    else:
        mid = (left + right) // 2
        left_node = init(node * 2, left, mid)
        right_node = init(node * 2 + 1, mid + 1, right)
        arr[node] = left_node + right_node
        return arr[node]

def subSum(node, f, t, left, right):

    if right < f or t < left:
        return 0
    
    if left <= f and t <= right:
        return arr[node]

    mid = (f + t) // 2
    left_sum = subSum(node * 2, f, mid, left, right)
    right_sum = subSum(node * 2 + 1, mid + 1, t, left, right)
    return left_sum + right_sum

def update(node, f, t, index, diff):

    if index < f or t < index:
        return
    
    arr[node] += diff

    if f != t:    
        mid = (f + t) // 2
        update(node * 2, f, mid, index, diff)
        update(node * 2 + 1, mid + 1, t, index, diff)

N, M, K = map(int, input().rstrip().split())
    
tmp = []
arr = [0] * 4 * N

for _ in range(N):
    tmp.append(int(input().rstrip()))

init(1, 0, N - 1)

for _ in range(M + K):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        b = b - 1
        diff = c - tmp[b]
        tmp[b] = c
        update(1, 0, N - 1, b, diff)
    else:
        print(subSum(1, 0, N - 1, b - 1, c - 1))