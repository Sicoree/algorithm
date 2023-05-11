dict = {
    0 : '1',
    1 : '2',
    2 : '4'
    }

def solution(n):
    answer = ''
    x = n - 1
    
    while True:
        x, mod = divmod(x, 3)

        answer += dict[mod]

        if x == 0:
            break
        
        x = x - 1
        
    return answer[::-1] 