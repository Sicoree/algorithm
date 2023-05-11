def solution(progresses, speeds):
    answer = []
    cut = len(progresses)
    idx = 0
    while idx < cut:
        cnt = 0
        
        if progresses[idx] >= 100:
            while idx < cut and progresses[idx] >= 100:
                    cnt += 1
                    idx += 1
            answer.append(cnt)
        
        for i in range(idx, cut):
            progresses[i] += speeds[i]        
            
    return answer