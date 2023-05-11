def solution(id_list, report, k):
    l = len(id_list)
    t = [i for i in range(l)]
    r = dict(zip(id_list, t))
    v_1 = [[0] * l for _ in range(l)]
    v_2 = [0] * l
    answer = [0] * l
    
    for i in report:
        A, B = i.split(' ')
        if v_1[r[A]][r[B]] != 1:
            v_1[r[A]][r[B]] = 1
            v_2[r[B]] += 1
        
    for i in range(l):
        if v_2[i] >= k:
            for j in range(l):
                if v_1[j][i] == 1: 
                    answer[j] += 1
                    
    return answer