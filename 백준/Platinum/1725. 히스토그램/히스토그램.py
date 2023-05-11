import sys

# 없으면 에러
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 인덱스까지 다루기 때문에 min, idx 를 쌍으로 가지고 있어야 함
def minIndex(left, right):
    if left[0] < right[0]:
        return left
    else:
        return right

# 구간별 최솟값 세그먼트 트리
def init(node, left, right):
    if left == right:
        arr[node] = [tmp[left], left]
        return arr[node]
    
    mid = (left + right) // 2
    left_node = init(node * 2, left, mid)
    right_node = init(node * 2 + 1, mid + 1, right)
    arr[node] = minIndex(left_node, right_node)
    return arr[node]

# node, from, to, left, right
# from, to = 현 노드의 범위
# left, right = 구해야하는 범위
def sol(node, f, t, left, right):
    if right < f or t < left:
        return [1000000001, -1]

    if left <= f and t <= right:
        return arr[node]
    
    mid = (f + t) // 2
    left_node = sol(node * 2, f, mid, left, right)
    right_node = sol(node * 2 + 1, mid + 1, t, left, right)
    return minIndex(left_node, right_node)

# node, from, to
# from, to = 현 노드의 범위
def divide(f, t):
    if f == t:
        return tmp[f]
    if f > t:
        return -1
    
    min, idx = sol(1, 0, N - 1, f, t)
    a = divide(f, idx - 1)
    b = divide(idx + 1, t)
    c = min * (t - f + 1)
    return max(a, b, c)

N = int(input())

tmp = []
for _ in range(N):
    tmp.append(int(input()))


arr = [[0] * 2 for _ in range(4 * N)]

init(1, 0, N - 1)
print(divide(0, N - 1))