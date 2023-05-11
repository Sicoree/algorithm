from heapq import *

def solution(scoville, K):
    cnt = 0
    h = []
    
    for value in scoville:
        heappush(h, value)
        
    while h[0] < K and len(h) > 1:
        heappush(h, heappop(h) + heappop(h) * 2)
        cnt += 1
    
    return cnt if h[0] >= K else -1

# def solution(scoville, K):
#     answer = -1
    
#     scoville.sort()
#     l = len(scoville)
#     idx = 0
    
#     while idx < l:
#         if scoville[idx] >= 7:
#             answer = idx
#             break
        
#         scoville[idx + 1] = scoville[idx] * 2 + scoville[idx + 1]
#         idx += 1
#         scoville.sort()
    
#     return answer