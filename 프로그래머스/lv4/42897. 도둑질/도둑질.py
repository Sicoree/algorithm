def solution(money):
    l = len(money)
    arr = [0 for _ in range(l)]   
    
    arr[0] = 0
    arr[1] = money[1]
    for idx in range(2, l):
        arr[idx] = max(arr[idx - 2] + money[idx], arr[idx - 1])

    arr[0] = money[0]
    arr[1] = money[0]
    for idx in range(2, l - 1):
        arr[idx] = max(arr[idx - 2] + money[idx], arr[idx - 1])
        
    return max(arr[-1], arr[-2])