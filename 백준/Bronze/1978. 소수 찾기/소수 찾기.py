N = int(input())
numbers = map(int, input().split())
result = 0
for num in numbers:
    if num == 2 or num == 3:
        result += 1
    elif num > 3:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            result += 1
print(result)