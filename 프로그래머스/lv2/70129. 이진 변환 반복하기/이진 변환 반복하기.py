def solution(s):
    cnt_z = 0
    cnt = 0
    while s != '1':
        cnt_z += s.count('0')
        cnt += 1
        s = bin(len(''.join(s.split('0'))))[2:]
        
    answer = [cnt, cnt_z]
    return answer