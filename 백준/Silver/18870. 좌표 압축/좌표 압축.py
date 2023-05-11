# 18870 / 좌표 압축
# https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arrsort = list(set(arr))
arrsort.sort()
arrnum = [i for i in range(len(arrsort))]

dict = dict(zip(arrsort, arrnum))

for x in arr:
    print(dict[x], end=' ')