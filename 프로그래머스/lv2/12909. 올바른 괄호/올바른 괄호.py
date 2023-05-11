def solution(s):
    cnt = 0
    
    for str in s:
        if cnt == -1:
            return False
            break
            
        if str == '(':
            cnt += 1
        elif str == ')':
            cnt -= 1
    
    if cnt == 0: 
        return True
    else:
        return False