n = int(input())

i = 1
cnt = 1
while n > i :
    i += 6 * cnt
    cnt += 1
print(cnt)