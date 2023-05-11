def solution(record):
    answer = []
    arr = []
    dict = {}
    
    for idx in record:
        tmp = list(idx.split(' '))
        if tmp[0] == 'Enter':
            arr.append([1, tmp[1]])
            dict[tmp[1]] = tmp[2]
        elif tmp[0] == 'Leave':
            arr.append([2, tmp[1]])
        elif tmp[0] == 'Change':            
            dict[tmp[1]] = tmp[2]
                                
    for tmp in arr:
        if tmp[0] == 1:
            answer.append('%s님이 들어왔습니다.' %dict[tmp[1]])
        elif tmp[0] == 2:
            answer.append('%s님이 나갔습니다.' %dict[tmp[1]])
    
    return answer