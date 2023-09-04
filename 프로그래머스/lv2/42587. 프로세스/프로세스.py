from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    answer = 0
    while q:
        top_p = max(q)
        cl = q.popleft()
        location -= 1 
        if cl != top_p:
            q.append(cl)
            if location < 0:
                location = len(q) -1
        else:
            answer += 1
            if location < 0:
                break
            
    return answer